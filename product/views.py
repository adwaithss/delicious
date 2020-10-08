from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *


class ProductlistPage(TemplateView):
    template_name = "product/productlist.html"

    def get(self, request, *args, **kwargs):
    	product = Product.objects.all().order_by('id')
    	context = {'product' : product}
    	return render(request, self.template_name, context) 


class ProductPage(TemplateView):
    template_name = "product/product.html"

    def get(self, request, slug, *args, **kwargs):
    	product = Product.objects.get(slug=slug)
    	context = {'product':product}
    	return render(request, self.template_name, context)


class CartPage(TemplateView):
    template_name = "product/cart.html"

    def get(self, request, *args, **kwargs):
    	return render(request, self.template_name)


class WishlistPage(TemplateView):
    template_name = "product/wishlist.html"

    def get(self, request, *args, **kwargs):
    	return render(request, self.template_name)

