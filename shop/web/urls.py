from django.urls import path
from .views import MainPageView, ShopPageView, ShopItemPageView, \
    ShopCommentItemPage, ShopItemSendCommentView, ShopCommentEditPage

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('shop/<int:pk>/edit_comment/<int:pk_alt>/',
         ShopCommentEditPage.as_view(), name='shop_item_edit_comment_page'),
    path('shop/<int:pk>/send_comment', ShopItemSendCommentView.as_view(),
         name='product_comment'),
    path('shop/<int:pk>/comments/', ShopCommentItemPage.as_view(),
         name='shop_item_comment_page'),
    path('shop/<int:pk>', ShopItemPageView.as_view(), name='shop_item_page'),
    path('shop/', ShopPageView.as_view(), name='shop_page'),
]
