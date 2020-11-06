from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', OrdersPage.as_view(), name='orders'),
    path('create/', CreateOrder.as_view(), name='create-order'),
]