from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile', 'updatedDate', 'createdDate']
    list_filter  = ['updatedDate', 'createdDate']
    ordering = ['-createdDate']
    search_fields = ['pin']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'createdDate']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'createdDate']


class RequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'dish_name', 'mobile', 'createdDate']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Request, RequestAdmin)