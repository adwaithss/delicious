from django.db import models
from django.contrib.auth.models import User
from authentication.models import UserProfile
from product.models import Product


class CheckOut(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	txnid = models.CharField(max_length=120)
	total = models.FloatField(default=0.0)
	is_active = models.BooleanField(default=True)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.txnid)


class Cart(models.Model):
	checkout = models.ForeignKey(CheckOut, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	price = models.FloatField()
	discount = models.FloatField(default=0.0)
	tax = models.FloatField(default=0.0)
	quantity = models.IntegerField()
	is_active = models.BooleanField(default=True)
	is_ordered = models.BooleanField(default=False)
	is_cancel = models.BooleanField(default=False)
	total = models.FloatField()
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product.name


class Order(models.Model):
	checkout = models.ForeignKey(CheckOut, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	total = models.FloatField()
	tax = models.FloatField()
	discount = models.FloatField()
	shipping_charge = models.FloatField()
	shipping_address = models.TextField()
	status = models.CharField(max_length=50)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.user.first_name


class Wishlist(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.user.user.first_name