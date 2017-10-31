import math
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader

from seraphim.characters.models import Character
from .models import Combat, StatusEffect, Wound, Heal
from .forms import WoundForm, HealForm, CombatForm



# Create your views here.
@login_required
def index(request):
    combat_list_in_progress = Combat.objects.filter(in_progress=True)
    combat_list_complete = Combat.objects.filter(in_progress=False)
    context = {
        'combat_list_in_progress': combat_list_in_progress,
        'combat_list_complete': combat_list_complete,
    }
    return render(request, 'tracker/index.html', context)


@login_required
def manage_combat(request, pk):
    combat = get_object_or_404(Combat, pk=pk)
    state = combat_state(combat)
    state.sort(key=lambda state: state[0].name)
    state.sort(key=lambda state: state[0].icon.sort_key)
    context = {}
    context['combat'] = combat
    context['combat_state'] = state
    return render(request, 'tracker/manage_combat.html', context)


@login_required
def character_detail(request, combat_pk, character_pk):
    context = {}
    combat = get_object_or_404(Combat, pk=combat_pk)
    character = get_object_or_404(Character, pk=character_pk)
    current_hp, max_hp, total_h = character_state(combat, character)
    damage = max_hp.hp - current_hp.hp
    remaining_h = max(max_hp.hp-total_h, 0)
    if remaining_h == 0:
        messages.error(request, '''
            This character has already been healed for {} points today.  Any
            further healing will require a CON save to avoid death!
        '''.format(total_h, ))
    elif remaining_h < damage:
        messages.warning(request, '''
            This character has {} damage, and has already taken {} points
             of healing today.  Healing more than {} will require a CON 
             save to take the remainder of the healing.
        '''.format(damage, total_h, remaining_h))
    context['combat'] = combat
    context['character'] = character
    context['current_hp'] = current_hp
    context['max_hp'] = max_hp
    context['damage'] = damage
    context['total_h'] = total_h
    context['remaining_h'] = remaining_h
    context['woundform'] = WoundForm({
        'character': character,
        'combat': combat,
        'amount': 0,
    })
    context['healform'] = HealForm({
        'character': character,
        'combat': combat,
        'amount': min(remaining_h, damage),
    })
    return render(request, 'tracker/character_detail.html', context)

@login_required
def add_wound(request, combat_pk, character_pk):
    if request.method == 'POST':
        form = WoundForm(request.POST)
        if form.is_valid():
            #process as needed
            form.save()
    return redirect('tracker:manage', combat_pk)


@login_required
def add_heal(request, combat_pk, character_pk):
    if request.method == 'POST':
        form = HealForm(request.POST)
        if form.is_valid():
            #process as needed
            form.save()
    return redirect('tracker:manage', combat_pk)


@login_required
def bandage_character(request, combat_pk, character_pk):
    """
        POST to this view with 'skill_level' in bandaging, and 
        'bonus' hitpoints from superior tools to automatically bandage 
        the character.
    """    
    combat = get_object_or_404(Combat, pk=combat_pk)
    character = get_object_or_404(Character, pk=character_pk)
    if request.method == 'POST':
        bonus = int(request.POST['bonus'])
        skill_level = int(request.POST['skill_level'])
        damage = 0
        wounds = Wound.objects.filter(character=character, combat=combat, bandaged=False)
        for wound in wounds:
            damage += wound.amount
            wound.bandaged = True
            wound.save()
        # level 1 (Rudimentary) = Heal 1 per 8 damage, plus bonus
        # level 2 (Proficient) = Heal 1 per 7 damage, plus bonus
        # level 3 (Expert) = Heal 1 per 6 damage, plus bonus
        if damage > 0:
            healing = math.ceil(damage * (1/(9-skill_level)))
            healing += bonus
            bandage = Wound(combat=combat, character=character, amount=-healing, bandaged=True)
            bandage.save()
    return redirect('tracker:manage', combat_pk)


class CombatCreate(LoginRequiredMixin, CreateView):
    model = Combat
    success_url = reverse_lazy('tracker:index')
    form_class = CombatForm



# Pre-calculate some information to pass along to our templates
def combat_state(combat):
    """
    Get the current state of each combatant in the group.  Returns
    a list of tuples (Character, current_hp, max_hp, total_healed)
    """
    state = []
    for character in combat.group.members.all():
        current_hp, max_hp, total_h = character_state(combat, character)
        state.append((character, current_hp, max_hp, total_h))
    return state

def character_state(combat, character):
    """
        Get the combat status of a single character, as a tuple of
        current_hp, max_hp, total healing
    """
    max_hp = Max_hp(character.base_hp)
    total_h = 0
    for effect in StatusEffect.objects.filter(character=character, combat=combat, effect_typ__typ='MAX_HP'):
        max_hp.hp += effect.effect_val
    current_hp = Current_hp(max_hp.hp)
    for wound in Wound.objects.filter(character=character, combat=combat):
        current_hp.hp -= wound.amount
    for heal in Heal.objects.filter(character=character, combat=combat):
        current_hp.hp += heal.amount
        total_h += heal.amount
    return current_hp, max_hp, total_h


class Max_hp:
    def __init__(self, hp):
        self.hp = hp
        self.base_hp = hp

    def __str__(self):
        return str(self.hp)

    def style(self):
        style = "font-weight-light"
        if self.hp > self.base_hp:
            style += " text-success"
        elif self.hp < self.base_hp:
            style += " text-muted"
        return style


class Current_hp:
    def __init__(self, hp):
        self.hp = hp
        self.max_hp = hp

    def __str__(self):
        return str(self.hp)

    def style(self):
        style = "font-weight-bold"
        pct = self.hp / self.max_hp
        if pct >= 0.99:
            style += " "
        elif pct >= 0.90:
            style = ""
        elif pct >= 0.66:
            style += " text-success"
        elif pct >= 0.33:
            style += " text-warning"
        elif pct > 0.00:
            style += " text-danger"
        else:
            style = " text-danger "
        return style

    def outer_style(self):
        style = ""
        pct = self.hp / self.max_hp
        if pct < 0.00:
            style = "text-muted"
        return style
