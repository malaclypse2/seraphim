from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import six

from .models import Character, CharacterIcon
from .forms import CharacterForm


class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Character
    pk = 'id'

class CharacterList(ListView):
    model = Character
    ordering = ['icon__sort_key', 'name', ]
    def get_queryset(self):
        queryset = self.model._default_manager.all()
        queryset = Character.objects.filter(public=True)
        if self.request.user.is_authenticated():
            queryset |= Character.objects.filter(owner=self.request.user)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, six.string_types):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    success_url = reverse_lazy('characters:list')
    form_class = CharacterForm

    def get_initial(self):
        return {'owner': self.request.user}

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    success_url = reverse_lazy('characters:list')
    form_class = CharacterForm

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = reverse_lazy('characters:list')

