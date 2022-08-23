from django.urls import path
from .views import RegisterPageView, LoginPageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register_page'),
    path('login/', LoginPageView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
]
