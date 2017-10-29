from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader

from seraphim.characters.models import Character
from .models import Combat, StatusEffect, Wound, Heal



# Create your views here.
def index(request):
    combat_list_in_progress = Combat.objects.filter(in_progress=True)
    combat_list_complete = Combat.objects.filter(in_progress=False)
    context = {
        'combat_list_in_progress': combat_list_in_progress,
        'combat_list_complete': combat_list_complete,
    }
    return render(request, 'tracker/index.html', context)

def manage_combat(request, pk):
    combat = get_object_or_404(Combat, pk=pk)
    context = {}
    context['combat'] = combat
    context['combat_state'] = combat_state(combat)
    return render(request, 'tracker/manage_combat.html', context)

def character_detail(request, combat_pk, character_pk):
    context = {}
    combat = get_object_or_404(Combat, pk=combat_pk)
    character = get_object_or_404(Character, pk=character_pk)
    current_hp, max_hp, total_h = character_state(combat, character)
    context['combat'] = combat
    context['character'] = character
    context['current_hp'] = current_hp
    context['max_hp'] = max_hp
    context['damage'] = max_hp.hp - current_hp.hp
    context['total_h'] = total_h
    return render(request, 'tracker/character_detail.html', context)

def manage_wound(request, combat_pk, character_pk):
    context = {}
    combat = get_object_or_404(Combat, pk=combat_pk)
    character = get_object_or_404(Character, pk=character_pk)
    current_hp, max_hp, total_h = character_state(combat, character)
    context['combat'] = combat
    context['character'] = character
    context['current_hp'] = current_hp
    context['max_hp'] = max_hp
    context['damage'] = max_hp.hp - current_hp.hp
    context['total_h'] = total_h
    return render(request, 'tracker/character_wounds.html', context)


# Pre-calculate some information to pass along to our templates
def combat_state(combat):
    """
    Get the current state of each combatant in the group.  Returns
    a list of (Character, current_hp, max_hp)
    """
    state = []
    for character in combat.game_day.group.members.all():
        current_hp, max_hp, total_h = character_state(combat, character)
        state.append((character, current_hp, max_hp, total_h))
        state.sort(key=lambda state: state[0].level, reverse=True)
        state.sort(
            key=lambda state: state[1].max_hp - state[1].hp, reverse=True)
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
            style += " text-muted"
        return style
