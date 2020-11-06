from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', Dashboard.as_view(), name='dadhboard'),
	path('ordermanagement/', OrderManagement.as_view(), name='ordermanagement'),
]