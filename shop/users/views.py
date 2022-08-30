import logging

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from .forms import ProfileForm, CreateUserForm, LoginForm, ImageForm, \
    ProfileChangeForm, UsernameChangeForm
from .models import Profile, User
from web.models import CommentReviewAboutProduct, Bucket, Product
from web.forms import BucketForm


class RegisterPageView(View):
    template_name = 'users/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('login_page')
        return render(request, self.template_name,
                      {'profile_form': ProfileForm,
                       'user_form': CreateUserForm})

    def post(self, request):
        profile_form = ProfileForm(request.POST)
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            stud = profile_form.save(commit=False)
            stud.user = user_form.save()
            stud.save()
            logout(request)
            return redirect('login_page')
        return render(request, self.template_name,
                      {'profile_form': profile_form,
                       'user_form': user_form})


class LoginPageView(View):
    template = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main_page')
        return render(request, self.template,
                      {'login_form': LoginForm})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            if user:
                login(request, user)
                return redirect('profile_page')
        return render(request, self.template, {'login_form': form})


class ProfilePageView(LoginRequiredMixin, View):
    template = 'users/main_profile.html'
    login_url = 'login_page'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)

        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'user_comment': CommentReviewAboutProduct.objects.filter(
                           author=profile)})

    def post(self, request):
        CommentReviewAboutProduct.objects.filter(
            pk=request.POST.get('key')).first().delete()
        img_form = ImageForm(request.POST, request.FILES)
        profile = Profile.objects.get(user=request.user)
        if img_form.is_valid():
            img_form = img_form.save(commit=False)
            if img_form.img != 'no_image_django_shop_py.jpg':
                profile.img = img_form.img
                profile.save(update_fields=['img'])
            return redirect('profile_page')
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'errors': img_form},
                      )


class ProfilePersonalPageView(LoginRequiredMixin, View):
    template = 'users/personal_profile.html'
    login_url = 'login_page'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        form_profile = ProfileChangeForm(instance=profile)
        form_username = UsernameChangeForm(instance=profile.user)
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'form_profile': form_profile,
                       'form_username': form_username},
                      )

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(username=request.user)
        form_profile = ProfileChangeForm(request.POST, request=request)
        form_username = UsernameChangeForm(request.POST, request=request)
        if form_profile.is_valid() and form_username.is_valid():
            profile.first_name = form_profile.cleaned_data.get('first_name')
            profile.last_name = form_profile.cleaned_data.get('last_name')
            profile.email = form_profile.cleaned_data.get('email')
            user.username = form_username.cleaned_data.get('username')
            profile.save()
            user.save()
            return redirect('personal_page')
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'form_profile': form_profile,
                       'form_username': form_username},
                      )


class ProfileBucketPageView(View):
    template = 'users/bucket_profile.html'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        buckets = Bucket.objects.filter(
            owner=Profile.objects.get(user=request.user))
        buckets_form = [BucketForm(instance=bucket) for bucket in buckets]
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'buckets': buckets,
                       'buckets_form': buckets_form
                       })

    def post(self, request):
        self.request_checker(request)
        img_form = ImageForm(request.POST, request.FILES)
        profile = Profile.objects.get(user=request.user)
        # if bucket_form.is_valid():
        #     # Bucket.objects.get(owner=profile, product=)
        # pass
        if img_form.is_valid():
            img_form = img_form.save(commit=False)
            if img_form.img != 'no_image_django_shop_py.jpg':
                profile.img = img_form.img
                profile.save(update_fields=['img'])
            return redirect('bucket_page')
        return render(request, self.template,
                      {'profile_model': profile,
                       'img': ImageForm,
                       'errors': img_form},
                      )

    def request_checker(self, request):
        logging.error(request.POST)
        if x := request.POST.get('key'):
            Bucket.objects.get(pk=x).delete()
        elif x := request.POST.get('plus'):
            bucket = Bucket.objects.get(pk=x)
            if bucket.quantity == 300:
                return
            bucket.quantity += 1
            bucket.save()
        elif x := request.POST.get('minus'):
            bucket = Bucket.objects.get(pk=x)
            if bucket.quantity == 1:
                bucket.delete()
                return
            bucket.quantity -= 1
            bucket.save()
        else:
            for ele in request.POST:
                if 'key' in ele:
                    quantity = int(request.POST[ele])
                    product = ele.replace('key ', '')
                    if 0 <= quantity <= 300:
                        bucket = Bucket.objects.get(
                            product=Product.objects.get(name=product),
                            owner=Profile.objects.get(user=request.user))
                        bucket.quantity = quantity
                        bucket.save()
                        return
