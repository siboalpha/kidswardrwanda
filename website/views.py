from django.shortcuts import redirect, render
from .models import Product, Order
from .forms import OrderForm, ContactForm
# Create your views here.

def index(request):
    page_title = 'Kids World Rwanda | Welcome'
    products = Product.objects.all()
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'page_title':page_title, 'products':products, 'form':form}
    return render(request, 'index.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')

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
            orderfrom = form.save(commit = False)
            orderfrom.product = product
            orderfrom.order_total = product.price
            form.save()
            instance = form.save()
            return redirect('order-received', pk=instance.pk)
    product_title = product.title
    page_title =  product_title + ' | Kids World Rwanda'
    context = {'page_title': page_title, 'product':product, 'form':form}
    return render(request, 'order-from.html', context)


def orderReceived(request, pk):
    order = Order.objects.get(id=pk)
    total = float(order.order_total)
    print(total)
    context = {'order': order, 'total':total}
    return render(request, 'order-received.html', context)