from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View


# Create your views here.
class TestView(View):
    def get(self, request):
        return HttpResponse('Hello world')
