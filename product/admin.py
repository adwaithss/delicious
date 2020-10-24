from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'createdDate', 'updatedDate']
    list_filter  = ['createdDate', 'updatedDate']
    ordering = ['-createdDate']
    search_fields = ['name', 'createdDate', 'updatedDate']


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'createdDate', 'updatedDate']
    list_filter  = ['createdDate', 'updatedDate']
    ordering = ['-createdDate']
    search_fields = ['name', 'createdDate', 'updatedDate']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'createdDate', 'updatedDate']
    list_filter  = ['createdDate', 'updatedDate']
    ordering = ['-createdDate']
    search_fields = ['name', 'createdDate', 'updatedDate']


class TaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'tax', 'createdDate', 'updatedDate']
    list_filter  = ['createdDate', 'updatedDate']
    ordering = ['-createdDate']
    search_fields = ['name', 'tax','createdDate', 'updatedDate']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'total', 'disc_total', 'quantity', 'status', 'stock', 'createdDate', 'updatedDate']
    list_filter  = ['createdDate', 'updatedDate']
    ordering = ['-createdDate']
    search_fields = ['name', 'disc_total', 'total', 'status', 'stock', 'createdDate', 'updatedDate']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Product, ProductAdmin) 