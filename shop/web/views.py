import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Bucket
from .forms import BucketForm
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
                                                 'teams': self.teams})


class ShopPageView(View):
    products = Product.objects.all()

    def get(self, request):
        return render(request, 'web/shop.html',
                      {'products': self.products})


class ShopItemPageView(View):
    template = 'web/shop_item_detail.html'

    def get(self, request, pk):
        return render(request, self.template,
                      {'product': get_object_or_404(Product, pk=pk),
                       'bucket_model': Bucket.objects.filter(
                           owner=Profile.objects.get(user=request.user),
                           product=get_object_or_404(Product, pk=pk),
                        ), }
                      )

    def post(self, request, pk):
        # quantity = BucketForm(request.POST)
        profile_obj = Profile.objects.get(user=request.user)
        product_obj = get_object_or_404(Product, pk=pk)

        if not Bucket.objects.filter(product=product_obj,
                                     owner=profile_obj).exists():
            Bucket(owner=profile_obj, product=product_obj, quantity=1).save()
            return redirect('shop_item_page', pk=pk)
        #
        # if not quantity.is_valid():
        #     return render(request, self.template,
        #                   {'product': product_obj,
        #                    'bucket': quantity})
        #
        # bucket = Bucket.objects.get(product=product_obj,
        #                             owner=profile_obj)
        # bucket.quantity += quantity.cleaned_data.get('quantity')
        # bucket.save()
        # return redirect('shop_item_page', pk=pk)
        # #
