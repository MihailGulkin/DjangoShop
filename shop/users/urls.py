from django.urls import path
from .views import RegisterPageView, LoginPageView

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register_page'),
    path('login/', LoginPageView.as_view(), name='login_page')
]
