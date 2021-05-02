from django import forms
from django.forms import fields
from django.forms.widgets import SelectMultiple

from .models import Profile,Role


class ProfileUpdateForm(forms.ModelForm):
    role = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Role.objects.all()
               )
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'nickname', 'role']
       