import logging

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from .forms import ProfileForm, CreateUserForm, LoginForm


class RegisterPageView(View):
    template_name = 'users/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('login_page')
        return render(request, self.template_name,
                      {'profile_form': ProfileForm,
                       'user_form': CreateUserForm})

    def post(self, request):
        profile_form = ProfileForm(request.POST)
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            if profile_form.is_valid():
                stud = profile_form.save(commit=False)
                stud.user = user_form.save()
                stud.save()
                logout(request)
                return redirect('login_page')
        return render(request, self.template_name,
                      {'profile_form': profile_form,
                       'user_form': user_form})


class LoginPageView(View):
    template = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main_page')
        return render(request, self.template,
                      {'login_form': LoginForm})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            if user:
                login(request, user)
                return redirect('main_page')
        return render(request, self.template, {'login_form': form})


class ProfilePageView(View):
    def get(self, request):
        return HttpResponse('Hey')