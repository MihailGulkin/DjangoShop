from django.urls import path
from .views import MainPageView, ShopPageView, ShopItemPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('shop/<int:pk>', ShopItemPageView.as_view(), name='shop_item_page'),
    path('shop/', ShopPageView.as_view(), name='shop_page'),
]
