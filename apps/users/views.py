from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Profile

from .forms import ProfileUpdateForm


class ProfileDetailView(DetailView):
    model = Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm


class ProfileListView(ListView):
    model = Profile
