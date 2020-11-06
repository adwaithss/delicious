from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import *
from product.models import *
from order.models import *
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.template import RequestContext, loader


# @require_http_methods(["POST"])
class CreateOrder(CreateView):
    def get(self, request):
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        checkout = CheckOut.objects.get(txnid=request.POST['checkout'])
        order = Order()
        order.checkout = checkout
        order.user = request.user.userprofile
        order.total = request.POST['total']
        order.tax = request.POST['tax']
        order.discount = request.POST['discount']
        order.shipping_charge = 40
        order.shipping_address = request.user.userprofile.address + "\n" + request.user.userprofile.district + "\n" + request.user.userprofile.state + "\n" + request.user.userprofile.country + "\n" + request.user.userprofile.pin
        order.status = 'Order Placed'
        order.save()

        CheckOut.objects.filter(txnid=request.POST['checkout']).update(is_active=False)
        Cart.objects.filter(checkout=checkout).update(is_active=False)

        for x in Cart.objects.filter(checkout=checkout).all():
            product = Product.objects.get(id=x.product_id)
            product.quantity = (product.quantity) - x.quantity
            product.save()

        user = request.user.userprofile
        prd_cart = Cart.objects.filter(checkout=checkout, is_active=False)
        subject, from_email, to = 'Order Confirmed', 'Delicious Rolls <testbyadwaith@gmail.com>', [user.user.email]
        html_message = loader.render_to_string(str(settings.BASE_DIR) + '/templates/mail/ordermail.html', 
            {'user': user, 'prd_cart': prd_cart, 'order': order})
        message = ''
        send_mail(subject, message, from_email, to, fail_silently=False, html_message=html_message)
        return render(request, 'order/ordersuccess.html')


class OrdersPage(TemplateView):
    template_name = "order/orders.html"

    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user.userprofile).order_by('-id')
        cart = Cart.objects.filter(user=request.user.userprofile, is_active=False).order_by('-id')
        
        context = {'order': order, 'cart':cart}
        return render(request, self.template_name, context)


	

