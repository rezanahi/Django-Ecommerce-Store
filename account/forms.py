from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.CharField(max_length=100, help_text='Required', error_messages={'required': 'Enter an email'})
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)