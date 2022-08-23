from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from .forms import ProfileForm, CreateUserForm


class LoginPageView(View):
    def get(self, request):
        return render(request, 'users/login.html',
                      {'profile_form': ProfileForm,
                       'user_form': CreateUserForm})
