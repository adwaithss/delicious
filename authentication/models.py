from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobile = models.CharField(max_length=13)
	address = models.TextField(null=True)
	district = models.CharField(max_length=40, null=True)
	state = models.CharField(max_length=40, null=True)
	country = models.CharField(max_length=40, null=True)
	pin = models.CharField(max_length=6, null=True)
	avatar = models.ImageField(upload_to='user_avatar', null=True)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)


	def __str__(self):
		return '{} {}' .format(self.user.first_name, self.user.last_name).title()


class Banner(models.Model):
	name = models.CharField(max_length=225)
	image = models.ImageField(upload_to='banner', max_length=100)                                                                         
	url = models.CharField(max_length=225, default='#')
	description = models.TextField()
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name


	