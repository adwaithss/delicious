from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile', 'updatedDate', 'createdDate']
    list_filter  = ['updatedDate', 'createdDate']
    ordering = ['-createdDate']
    search_fields = ['pin']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'createdDate']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Banner, BannerAdmin)