from django import forms

from  movies.models import *


class AuthenticationForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.CharField(max_length=300, required=True, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
