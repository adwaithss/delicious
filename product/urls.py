from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', ProductlistPage.as_view(), name='dishes'),
    path('<str:slug>/', ProductPage.as_view(), name='product'),
]