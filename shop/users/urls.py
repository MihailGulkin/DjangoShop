from django.urls import path
from .views import LoginPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login_page'),
]
