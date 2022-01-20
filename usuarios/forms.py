from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Usuario

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__' 