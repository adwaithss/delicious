from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import os
import base64
from django.template import RequestContext, loader
from django.conf import settings
from product.models import *
from django.core.mail import send_mail
from order.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Dashboard(TemplateView):
    template_name = "administrator/home.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        
        context = {}
        return render(request, self.template_name, context)


class OrderManagement(TemplateView):
    template_name = "administrator/orders.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        order = Order.objects.all().order_by('-id')

        paginator = Paginator(order, 6)
        page = request.GET.get('page')

        try:
            order = paginator.page(page)
        except PageNotAnInteger:
            order = paginator.page(1)
        except EmptyPage:
            order = paginator.page(paginator.num_pages)

        context = {'order': order}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        print(request.POST['checkout'])
        order = Order.objects.get(checkout__txnid=request.POST['checkout'])
        order.status = request.POST['status']
        order.save()
        return redirect('/administrator/ordermanagement/')
