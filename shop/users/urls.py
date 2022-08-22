from django.urls import path, include
from .views import TestView

urlpatterns = [
    path('test/', TestView.as_view(), name='test_page'),
]
