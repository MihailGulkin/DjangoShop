from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


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
    def get(self, request, pk):
        return render(request, 'web/shop_item_detail.html',
                      {'product': get_object_or_404(Product, pk=pk)})
