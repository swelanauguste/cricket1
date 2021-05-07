from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .models import Item


class ItemList(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'


class ItemUpdate(UpdateView):
    model = Item
    fields = ['count', 'desc']
