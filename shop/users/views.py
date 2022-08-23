import logging

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View
from .forms import ProfileForm, CreateUserForm


class LoginPageView(View):
    def get(self, request):
        return render(request, 'users/login.html',
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
                return redirect('main_page')
            else:
                logging.getLogger(__name__).error('Ошибка')

        else:
            logging.getLogger(__name__).error(type(user_form))

        return render(request, 'users/login.html',
                          {'profile_form': profile_form,
                           'user_form': user_form})