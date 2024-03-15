from django.forms import ModelForm
from .models import Thread
from django import forms
from django.contrib.auth.models import User


# This form is used to create or update Thread instances.
class ThreadForm(ModelForm):
    class Meta:
        model = Thread  # Specifies the model to which the form is linked.
        fields = '__all__'  # Includes all fields from the model in the form.
        exclude = ['host', 'participants']


# This form could be used for user registration or updating user information,
class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Specifies the User model as the form's model.
        fields = ['username', 'email']
