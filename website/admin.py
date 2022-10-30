from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(productCategories)
class productCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category','date_created')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'client', 'client_phone_number','client_email', 'order_total')

@admin.register(ContactMessage)
class COntactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_created')
