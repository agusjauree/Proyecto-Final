
from django import forms
from .models import Libro
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
 

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       