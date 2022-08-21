from django.urls import path, include
from .views import MainPageView, ShopPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('shop/', ShopPageView.as_view(), name='shop_page'),
]
