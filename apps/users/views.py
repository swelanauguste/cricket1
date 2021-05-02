from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profile

from .forms import ProfileUpdateForm


class ProfileDetailView(DetailView):
    model = Profile


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user

    def handle_no_permission(self):
        return redirect("/")


class ProfileListView(ListView):
    model = Profile
    queryset = Profile.objects.filter(is_active=True)
