from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from .forms import ProfileForm, CreateUserForm


class TestView(View):
    def get(self, request):
        return render(request, 'users/test.html', {'form': ProfileForm,
                                                   'userform': CreateUserForm})
