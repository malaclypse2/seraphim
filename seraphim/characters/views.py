from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Character

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the characters index.")

class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character

class CharacterListView(LoginRequiredMixin, ListView):
    model = Character