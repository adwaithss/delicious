from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


class ProductlistPage(ListView):
    template_name = "product/productlist.html"

    def get(self, request, *args, **kwargs):
        product = Product.objects.all().order_by('-id')

        paginator = Paginator(product, 6)
        page = request.GET.get('page')

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        context = {'product' : product}
        return render(request, self.template_name, context) 


class ProductPage(TemplateView):
    template_name = "product/product.html"

    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        related_product = Product.objects.filter(category=product.category).exclude(id=product.id).all().order_by('-id')
        context = {'product':product, 'related_product':related_product}
        return render(request, self.template_name, context)

