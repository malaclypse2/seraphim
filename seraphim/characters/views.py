from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse

from .models import Character


class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Character
    pk = 'id'

class CharacterList(LoginRequiredMixin, ListView):
    model = Character

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    success_url = reverse_lazy('characters:list')
    fields = '__all__'

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    success_url = reverse_lazy('characters:list')
    fields = '__all__'

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = reverse_lazy('characters:list')

