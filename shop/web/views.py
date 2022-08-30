import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Bucket, CommentReviewAboutProduct
from .forms import BucketForm, CommentReviewForm
from users.models import Profile


class MainPageView(View):
    # region important
    objects = {'object_1': ['image/paw.svg',
                            'СМАРТФОНЫ',
                            'Mobile'],
               'object_2': ['image/gear.svg',
                            'НОУТБУКИ',
                            'Notebook'],
               'object_3': ['image/apple.svg',
                            'КОМПЬЮТЕРЫ',
                            'PC'],
               'object_4': ['image/medKit.svg',
                            'АКСЕССУАРЫ',
                            'Accessories']}
    teams = {'team_lead_1': ['image/team_lead_1.jpg',
                             'SKYLER WHITE',
                             'Accountant',
                             'Lorem ipsum dolor sit amet, consectetur '
                             'adipiscing elit. Proin consequat sollicitudin '
                             'cursus. Dolor sit amet, consectetur adipiscing '
                             'elit proin consequat.', ],
             'team_lead_2': ['image/team_lead_2.jpg',
                             'JOHN PARKER',
                             'Leading Specialist',
                             'Lorem ipsum dolor sit amet, consectetur '
                             'adipiscing elit. Proin consequat sollicitudin '
                             'cursus. Dolor sit amet, consectetur adipiscing '
                             'elit proin consequat.', ],
             'team_lead_3': ['image/team_lead_3.jpg',
                             'MARC DOE',
                             'Team Leader',
                             'Lorem ipsum dolor sit amet, consectetur '
                             'adipiscing elit. Proin consequat sollicitudin '
                             'cursus. Dolor sit amet, consectetur adipiscing '
                             'elit proin consequat.']}

    # endregion

    def get(self, request):
        return render(request, 'web/main.html', {'objects': self.objects,
                                                 'teams': self.teams,
                                                 })


class ShopPageView(View):
    template = 'web/shop.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template,
                      {'products': products})


class ShopItemPageView(LoginRequiredMixin, View):
    template = 'web/shop_item_detail.html'
    login_url = 'login_page'

    def get(self, request, pk):
        return render(request, self.template,
                      {'product': get_object_or_404(Product, pk=pk),
                       'bucket_model': Bucket.objects.filter(
                           owner=Profile.objects.get(user=request.user),
                           product=get_object_or_404(Product, pk=pk),
                       ),
                       'comments': CommentReviewAboutProduct.objects.filter(
                           product=get_object_or_404(Product, pk=pk))}
                      )

    def post(self, request, pk):
        profile_obj = Profile.objects.get(user=request.user)
        product_obj = get_object_or_404(Product, pk=pk)

        if not Bucket.objects.filter(product=product_obj,
                                     owner=profile_obj).exists():
            Bucket(owner=profile_obj, product=product_obj, quantity=1).save()
        return redirect('shop_item_page', pk=pk)


class ShopCommentItemPage(View):
    template = 'web/shop_item_detail_comments.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        profile = Profile.objects.get(user=request.user)
        return render(request, self.template,
                      {'product': product,
                       'bucket_model': Bucket.objects.filter(
                           owner=profile,
                           product=product, ),
                       'comment_form': CommentReviewAboutProduct.objects.filter
                       (product=product),
                       'comments': CommentReviewAboutProduct.objects.filter(
                           product=get_object_or_404(Product, pk=pk))
                       }
                      )

    def post(self, request, pk):
        profile_obj = Profile.objects.get(user=request.user)
        product_obj = get_object_or_404(Product, pk=pk)

        if not Bucket.objects.filter(product=product_obj,
                                     owner=profile_obj).exists():
            Bucket(owner=profile_obj, product=product_obj, quantity=1).save()
        return redirect('shop_item_comment_page', pk=pk)


class ShopItemSendCommentView(View):
    template = 'web/send_comment.html'

    def get(self, request, pk):
        return render(request, self.template,
                      {'product_review': CommentReviewForm()})

    def post(self, request, pk):
        comment_form = CommentReviewForm(request.POST)
        if comment_form.is_valid():
            sub_form = comment_form.save(commit=False)
            sub_form.author = Profile.objects.get(user=request.user)
            sub_form.product = Product.objects.get(pk=pk)
            sub_form.save()
            return redirect('shop_item_comment_page', pk=pk)
        return render(request, self.template,
                      {'product_review': comment_form})


class ShopCommentEditPage(View):
    template = 'web/shop_item_comment_edit.html'

    def get(self, request, pk, pk_alt):
        comment_model = CommentReviewAboutProduct.objects.filter(
            product=Product.objects.get(pk=pk), pk=pk_alt).first()
        comment_form = CommentReviewForm(instance=comment_model)
        return render(request, self.template,
                      {'product_review': comment_form})

    def post(self, request, pk, pk_alt):
        comment_form = CommentReviewForm(request.POST)
        comment_edit = CommentReviewAboutProduct.objects.filter(
            product=Product.objects.get(pk=pk), pk=pk_alt).first()
        if comment_form.is_valid():
            comment_edit.product_cons = comment_form.cleaned_data.get('product_cons')
            comment_edit.product_pros = comment_form.cleaned_data.get('product_pros')
            comment_edit.product_comment = comment_form.cleaned_data.get('product_comment')
            comment_edit.save()
            return redirect('profile_page')
        return render(request, self.template,
                      {'product_review': comment_form})