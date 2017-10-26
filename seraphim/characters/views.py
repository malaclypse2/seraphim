from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse

from .models import Character


def index(request):
    return HttpResponse("Hello, world. You're at the characters index.")

class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character
    pk = 'id'

class CharacterListView(LoginRequiredMixin, ListView):
    model = Character
