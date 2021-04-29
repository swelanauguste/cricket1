from django.urls import path

from .views import (ProfileDetailView, ProfileListView, ProfileUpdateView)


app_name = 'users'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list'),
    path('<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='profile-update'),
]
