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


class Dashboard(TemplateView):
    template_name = "administrator/home.html"

    def get(self, request, *args, **kwargs):
        
        context = {}
        return render(request, self.template_name, context)