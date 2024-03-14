from django.forms import ModelForm
from .models import Thread
from django import forms
from django.contrib.auth.models import User

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']