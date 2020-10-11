from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from product.models import *


class HomePage(TemplateView):
    template_name = "common/home.html"

    def get(self, request, *args, **kwargs):
        product1 = Product.objects.all().order_by('-id')[0:3]
        product2 = Product.objects.all().order_by('-id')[3:6]
        banner = Banner.objects.all()
        
        context = {'product1': product1, 'product2':product2, 'banner':banner}
        return render(request, self.template_name, context)


class RegisterPage(TemplateView):
    template_name = "authentication/register.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if not User.objects.filter(email=request.POST['email']).count() == 0:
            context = {"message" : "Email already taken"}
            return render(request, self.template_name, context)
        elif not UserProfile.objects.filter(mobile=request.POST['mobile']).count() == 0:
            context = {"message" : "Mobile Number already taken"}
            return render(request, self.template_name, context)
        user = User()
        user.username = request.POST['email']
        user.email = request.POST['email']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.set_password(request.POST['password'])
        user.save()
        
        profile = UserProfile()
        profile.user = user
        profile.mobile = request.POST['mobile']
        profile.address = request.POST['address']
        profile.district = request.POST['district']
        profile.state = request.POST['state']
        profile.country = request.POST['country']
        profile.pin = request.POST['pin']
        profile.avatar = 'user_avatar/avatar.png'
        profile.save()
        
        return redirect('/thankyou')


class LoginPage(TemplateView):
    template_name = "authentication/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                context = {"message" : "User is not activeted yet, Please check the email for activation link"}
            return render(request, self.template_name, context)
        else:
            context = {"message" : "Invalid Email or Password"}
            return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class ProfileView(TemplateView):
	template_name = "authentication/profile.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class EditProfileView(TemplateView):
    template_name = "authentication/editprofile.html"
    def get(self, request, *args, **kwargs):
       context = {}
       return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()

        profile = UserProfile.objects.get(user=user)
        profile.mobile = request.POST['mobile']
        profile.address = request.POST['address']
        profile.district = request.POST['district']
        profile.state = request.POST['state']
        profile.pin = request.POST['pin']
        profile.save()

        return redirect('/profile')


class SuccessView(TemplateView):
	template_name = "authentication/thankyou.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class ContactView(TemplateView):
	template_name = "common/contact.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)




