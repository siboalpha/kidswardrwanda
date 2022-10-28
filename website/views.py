from django.shortcuts import redirect, render
from .models import Product, Order
from .forms import OrderForm
# Create your views here.

def index(request):
    page_title = 'Kids World Rwanda | Welcome'
    products = Product.objects.all()
    context = {'page_title':page_title, 'products':products}
    return render(request, 'index.html', context)

def shop(request):
    products = Product.objects.all()
    page_title = 'Shop kids toy with us | Kids World Rwanda'
    context = {'page_title': page_title, 'products':products}
    return render(request, 'shop.html', context)

def product(request, pk):
    product = Product.objects.get(id = pk)
    product_title = product.title
    page_title =  product_title + ' | Kids World Rwanda'
    context = {'page_title': page_title, 'product':product}
    return render(request, 'product.html', context)

def order(request, pk):
    form = OrderForm()
    product = Product.objects.get(id = pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            oderfom = form.save(commit = False)
            oderfom.product = product
            oderfom.order_total = product.price
            oderfom.save()
            instance = product
            return redirect('order-received', pk=instance.pk)
    product_title = product.title
    page_title =  product_title + ' | Kids World Rwanda'
    context = {'page_title': page_title, 'product':product, 'form':form}
    return render(request, 'order-from.html', context)


def orderReceived(request, pk):
    order = Order.objects.get(id=pk)
    total = float(order.order_total) * 2
    print(total)
    context = {'order': order, 'total':total}
    return render(request, 'order-received.html', context)