from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['checkout', 'user', 'total', 'status', 'createdDate']
    list_filter  = ['status', 'createdDate']
    ordering = ['-createdDate']
    search_fields = ['status']


class CartAdmin(admin.ModelAdmin):
    list_display = ['checkout', 'user', 'product', 'total', 'is_active', 'is_ordered', 'is_cancel', 'createdDate']
    list_filter  = ['checkout', 'user', 'product', 'createdDate']
    ordering = ['-createdDate']
    search_fields = ['total']


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['txnid', 'user', 'is_active', 'createdDate']
    list_filter  = ['txnid', 'user', 'is_active', 'createdDate']
    ordering = ['-createdDate']
    search_fields = ['txnid']


admin.site.register(Order, OrderAdmin)

admin.site.register(CheckOut, CheckoutAdmin)
admin.site.register(Cart, CartAdmin)
# admin.site.register(Order)