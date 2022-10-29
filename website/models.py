from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unicodedata import category
from django.db import models

# Create your models here.

class productCategories(models.Model):
    category = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.category

class Product(models.Model):
    recently_added = 'recently added'
    popular = 'popular'

    PLACEMENT_CHOICES = [
        (recently_added, 'recently added'),
        (popular, 'popular'),
    ]
    title = models.CharField(max_length = 255)
    product_image = models.ImageField(upload_to = 'product_images', null = True)
    placement = models.CharField(max_length = 255, choices = PLACEMENT_CHOICES, default = popular)
    price = models.FloatField(max_length = 8)
    category = models.ForeignKey(productCategories,max_length = 255, on_delete = models.CASCADE)
    price = models.CharField(max_length = 255)
    description = models.TextField(max_length = 500)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order_total = models.FloatField(max_length = 255, null=True, default = "0")
    client = models.CharField(max_length = 255)
    client_email = models.CharField(max_length = 255)
    client_phone_number = models.CharField(max_length = 255)
    client_address = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add = True, null = True)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    message = models.TextField(max_length = 500)
    date_created = models.DateTimeField(auto_now_add = True)
