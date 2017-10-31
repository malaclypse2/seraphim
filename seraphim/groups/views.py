from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse

from .models import Group
from .forms import GroupForm

# Create your views here.


class GroupDetail(LoginRequiredMixin, DetailView):
    model = Group
    pk = 'id'


class GroupList(ListView):
    model = Group


class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    form_class = GroupForm


class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    form_class = GroupForm


class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
