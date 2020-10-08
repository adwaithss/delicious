from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('', HomePage.as_view(), name='home'),
]
