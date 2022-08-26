import logging

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from .forms import ProfileForm, CreateUserForm, LoginForm, ImageForm
from .models import Profile


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
        if user_form.is_valid() and profile_form.is_valid():
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
                return redirect('profile_page')
        return render(request, self.template, {'login_form': form})


class ProfilePageView(LoginRequiredMixin, View):
    template = 'users/main_profile.html'
    login_url = 'login_page'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)

        return render(request, self.template, {'profile_model': profile,
                                               'img': ImageForm})

    def post(self, request):
        img_form = ImageForm(request.POST, request.FILES)
        profile = Profile.objects.get(user=request.user)
        if img_form.is_valid():
            img_form = img_form.save(commit=False)
            if img_form.img != 'no_image_django_shop_py.jpg':
                profile.img = img_form.img
                profile.save(update_fields=['img'])
            return redirect('profile_page')
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'errors': img_form},
                      )


class ProfilePersonalPageView(LoginRequiredMixin, View):
    template = 'users/personal_profile.html'
    login_url = 'login_page'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,},
                      )
