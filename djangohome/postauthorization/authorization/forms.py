from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'password')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
