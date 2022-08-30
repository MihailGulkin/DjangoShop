from django.urls import path, re_path
from .views import RegisterPageView, LoginPageView, ProfilePageView, \
    ProfilePersonalPageView, ProfileBucketPageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    re_path(r'register/?', RegisterPageView.as_view(), name='register_page'),
    re_path(r'login/?', LoginPageView.as_view(), name='login_page'),
    re_path(r'logout/?', LogoutView.as_view(), name='logout_page'),
    re_path(r'profile/bucket/?', ProfileBucketPageView.as_view(),
            name='bucket_page'),
    re_path(r'profile/personal/?', ProfilePersonalPageView.as_view(),
            name='personal_page'),
    re_path(r'profile/?', ProfilePageView.as_view(), name='profile_page'),
]
