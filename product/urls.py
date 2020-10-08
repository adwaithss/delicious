from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('dishes/', ProductlistPage.as_view(), name='dishes'),
    # path('product/', ProductPage.as_view(), name='product'),
    path('product/<str:slug>/', ProductPage.as_view(), name='product'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('wishlist/', WishlistPage.as_view(), name='wishlist'),
]