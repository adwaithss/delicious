from django.db import models
from slugify import slugify


class Category(models.Model):
	name = models.CharField(max_length=50)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Subcategory(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=50)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Tax(models.Model):
	name = models.CharField(max_length=50)
	tax = models.IntegerField()
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	STATUS = (
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Deleted', 'Deleted'),
    )
	name = models.CharField(max_length=225)
	slug = models.SlugField(max_length = 250, null = True, blank = True)
	description = models.TextField()
	category = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
	subCategory = models.ForeignKey(Subcategory, null=True, on_delete=models.SET_NULL)
	tag = models.ManyToManyField(Tag, null=True)
	tax = models.ForeignKey(Tax, null=True, on_delete=models.SET_NULL)
	price = models.FloatField()
	specialPrice = models.FloatField(default=0.0)
	cost = models.FloatField()
	disc_total = models.FloatField(default=0.0)
	total = models.FloatField(default=0.0)
	quantity = models.IntegerField()
	stock = models.BooleanField(default=True)
	status = models.CharField(max_length=10, choices=STATUS)
	image1 = models.ImageField(upload_to='product', max_length=100)
	image2 = models.ImageField(upload_to='product', max_length=100, null=True, blank=True)
	image3 = models.ImageField(upload_to='product', max_length=100, null=True, blank=True)
	image4 = models.ImageField(upload_to='product', max_length=100, null=True, blank=True)
	createdDate = models.DateTimeField(auto_now_add=True)
	updatedDate = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name) + "-" + slugify(self.category.name) + "-" + str(self.id)
		if self.specialPrice == 0.0:
			self.total = "{:.2f}".format(self.price * ( 1 + (self.tax.tax / 100)))
			self.disc_total =  0.0
		else:
			self.total = "{:.2f}".format(self.specialPrice * ( 1 + (self.tax.tax / 100)))
			self.disc_total = "{:.2f}".format(self.price * ( 1 + (self.tax.tax / 100)))
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
