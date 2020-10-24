from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', CreateOrder.as_view(), name='create-order'),
    path('orders/', OrdersPage.as_view(), name='orders'),
]