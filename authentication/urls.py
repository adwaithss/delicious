from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('verify-email/<str:slug>/', VerifyEmail.as_view(), name='verify-email'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('editprofile/', EditProfileView.as_view(), name='editprofile'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('wishlist/', WishlistPage.as_view(), name='wishlist'),
    path('add-cart/', AddToCart.as_view(), name='add-cart'),
    path('add-wishlist/', AddToWishlist.as_view(), name='add-wishlist'),
]
