from django.shortcuts import render
from .models import *
 
def Principal(request):
	context = {}
	return render(request, 'store/Principal.html', context)

def Tienda(request):
	products = Product.objects.all()
	context = {'products': products}	
	return render(request, 'store/Tienda.html', context)

def Carrito(request):
	
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(custumer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 }
		
	context = {'items':items, 'order':order}
	return render(request, 'store/Carrito.html', context)

def Checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(custumer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 }

	context = {'items':items, 'order':order}	
	return render(request, 'store/Checkout.html', context)

