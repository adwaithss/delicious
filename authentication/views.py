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
from .models import *
from product.models import *
from django.core.mail import send_mail
import uuid
from order.models import *
from django.http import JsonResponse


def get_cart(request):
    try:
        cart_count = Cart.objects.filter(user_id=request.user.userprofile.id, is_active=True).count()
    except:
        cart_count = 0
    return JsonResponse(cart_count) 


class HomePage(TemplateView):
    template_name = "common/home.html"

    def get(self, request, *args, **kwargs):
        product1 = Product.objects.all().order_by('-id')[0:3]
        product2 = Product.objects.all().order_by('-id')[3:6]
        banner = Banner.objects.all().order_by('-id')
        
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
        user.is_active = False
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
        
        token = base64.b64encode(bytes(user.email, 'utf-8')).decode("utf-8") 
        decode = base64.b64decode(token).decode()

        activation_link = "http://127.0.0.1:8000/verify-email/" + token + "/"
        user = User.objects.get(id=user.id)
        subject, from_email, to = 'Verify your email', 'Admin <testbyadwaith@gmail.com>', [user.email]
        html_message = loader.render_to_string(str(settings.BASE_DIR) + '/templates/mail/confirm_mail.html', 
            {'activation_link': activation_link, 'user': user})
        message = ''
        send_mail(subject, message, from_email, to, fail_silently=False, html_message=html_message)

        return render(request, 'authentication/thankyou.html')


class VerifyEmail(UpdateView):
    def get(self, request, slug):
        email = base64.b64decode(slug).decode()
        try:
            User.objects.filter(email=email).update(is_active=True)
        except:
            pass

        return HttpResponseRedirect('/')


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
        if 'delete_avatar' in request.POST:
            user = request.user.id
            profile = UserProfile.objects.get(user=user)
            profile.avatar = ""
            profile.save()
            return redirect('/editprofile')
        elif 'get_avatar' in request.POST:
            user = request.user.id
            profile = UserProfile.objects.get(user=user)
            profile_avatar = request.FILES['upload_avatar'].name
            ext = os.path.splitext(profile_avatar)[1]
            ext_c = '/user_avatar/' + str(user) + ext
            c = request.FILES.get('upload_avatar')
            path = settings.MEDIA_ROOT+'/'+ext_c
            destination = open(path, 'wb+')
            for chunk in c.chunks():
                destination.write(chunk)
                destination.close()
            profile.avatar = ext_c
            profile.save()
        else:
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


class CartPage(TemplateView):
    template_name = "authentication/cart.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        cart = Cart.objects.filter(is_active=True, user=request.user.userprofile).order_by('-id')
        total = 0
        for x in cart:
            total += x.total
        context = {'cart': cart, 'total':total}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'cart_remove' in request.POST:
            cart = Cart.objects.filter(id=request.POST['cart'])
            cart.delete()
        return redirect('/cart/')


class WishlistPage(TemplateView):
    template_name = "authentication/wishlist.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        wishlist = Wishlist.objects.filter(user=request.user.userprofile).order_by('-id')
        context = {'wishlist': wishlist}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'wishlist_remove' in request.POST:
            wishlist = Wishlist.objects.filter(id=request.POST['wishlist'])
            wishlist.delete()
        return redirect('/wishlist/')


class ContactView(TemplateView):
	template_name = "common/contact.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class AddToCart(CreateView):
    def post(self, request, *args, **kwargs):
        user = request.user.id
        product = Product.objects.get(id=request.POST['product'])
        quantity = request.POST['quantity']
        tax = product.tax
        if product.specialPrice == 0.0:
            total = float(product.price) * float(quantity)
            price = product.price
        else:
            total = float(product.specialPrice) * float(quantity)
            price = product.specialPrice
        
        checkout, created = CheckOut.objects.get_or_create(user=request.user.userprofile, is_active=True)
        checkout.user = request.user.userprofile
        if not len(checkout.txnid) == 0 :
            checkout.txnid = checkout.txnid
        else:
            checkout.txnid = uuid.uuid1().int >> 64
        checkout.total += total
        checkout.save()

        cart = Cart()
        cart.checkout = checkout
        cart.product = product
        cart.user = request.user.userprofile
        cart.price = price
        cart.quantity = quantity
        cart.total = total
        cart.save()

        return redirect('/cart/')


class AddToWishlist(CreateView):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=request.POST['product'])

        if Wishlist.objects.filter(product=product, user=request.user.userprofile).count() == 0:
            wishlist= Wishlist()
            wishlist.user = request.user.userprofile
            wishlist.product = product
            wishlist.save()

        return redirect('/wishlist/')
