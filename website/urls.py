import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('product/<pk>', views.product, name='product'),
    path('order/<pk>', views.order, name='order'),
    path('order-received/<pk>', views.orderReceived, name='order-received')
]