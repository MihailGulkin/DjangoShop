from django.urls import path, re_path
from .views import RegisterPageView, LoginPageView, ProfilePageView, \
    ProfilePersonalPageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    re_path('register/?', RegisterPageView.as_view(), name='register_page'),
    re_path('login/?', LoginPageView.as_view(), name='login_page'),
    re_path('logout/?', LogoutView.as_view(), name='logout_page'),
    re_path('profile/?', ProfilePageView.as_view(), name='profile_page'),
    re_path('profile/personal/?', ProfilePersonalPageView.as_view(),
            name='personal_page'),
]
