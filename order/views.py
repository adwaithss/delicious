from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import *
from product.models import *
from order.models import *
from django.core.mail import send_mail


class CreateOrder(TemplateView):
	template_name = "order/ordersuccess.html"

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

		send_mail(
		    'Subject here',
		    'Hii'user.first_name 'order placed' 'Total ₹' order.total,
		    'testbyadwaith@gmail.com',
		    [order.user.user.email],
		    fail_silently=False,
		)

		return render(request, self.template_name)


class OrdersPage(TemplateView):
    template_name = "order/orders.html"

    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user.userprofile).order_by('-id')
        cart = Cart.objects.filter(user=request.user.userprofile, is_active=False).order_by('-id')
        
        context = {'order': order, 'cart':cart}
        return render(request, self.template_name, context)


	

