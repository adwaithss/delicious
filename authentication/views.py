from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from product.models import *


class HomePage(TemplateView):
    template_name = "common/home.html"

    def get(self, request, *args, **kwargs):
    	product1 = Product.objects.all()[0:3]
    	product2 = Product.objects.all()[3:6]
    	banner = Banner.objects.all()
    	context = {'product1': product1, 'product2':product2, 'banner':banner}
    	return render(request, self.template_name, context)


class RegisterPage(TemplateView):
	template_name = "authentication/register.html"

	def get(self, request, *args, **kwargs):
		form = UserCreationForm
		context = {'form': form}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		user = User()
		user.username = request.POST['email']
		user.email = request.POST['email']
		user.first_name = request.POST['firstname']
		user.last_name = request.POST['lastname']
		# user.password = request.POST['password']
		user.save()
		user.set_password(request.POST['password'])
		profile = UserProfile()
		profile.user = user
		profile.mobile = request.POST['mobile']
		profile.address = request.POST['address']
		profile.district = request.POST['district']
		profile.state = request.POST['state']
		profile.country = request.POST['country']
		profile.pin = request.POST['pin']
		profile.save()
		return HttpResponse(request.POST['email'])


class LoginPage(TemplateView):
	template_name = "authentication/login.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)
