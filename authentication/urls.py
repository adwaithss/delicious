from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('thankyou/', SuccessView.as_view(), name='thankyou'),
]
