import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thank-you/', views.thankYou, name='thank-you'),
    path('shop', views.shop, name='shop'),
    path('<slug:slug>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('order/<pk>', views.order, name='order'),
    path('order-received/<pk>', views.orderReceived, name='order-received')
]