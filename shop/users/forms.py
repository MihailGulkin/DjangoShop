import logging

from django.forms import ModelForm
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'email', 'first_name', 'last_name']

    def clean(self):
        if self.cleaned_data.get('first_name') == \
                self.cleaned_data.get('last_name'):
            raise forms.ValidationError(
                'Sorry, first_name and second_name cannot be same'
            )
        if Profile.objects.filter(
                email=self.cleaned_data.get('email')).exists():
            raise forms.ValidationError(
                'Sorry, email already exist'
            )

        return self.cleaned_data


class ImageForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['img']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        user_sq = User.objects.filter(username=username)
        if not user_sq.count():
            raise forms.ValidationError(
                'Sorry, that login was invalid. Please try again.')
        if user is None:
            raise forms.ValidationError(
                "Sorry, that password was invalid. Please try again.")
        return self.cleaned_data

    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
