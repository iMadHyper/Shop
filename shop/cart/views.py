from django.shortcuts import render, redirect

from .models import CartItem
from products.models import Product


cart_template = 'cart/cart_items.html'

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {
        'cart_items' : cart_items
    }
    return render(request, cart_template, context)

def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()            
            
    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, product_slug):
    cart_item = CartItem.objects.get(user=request.user, product__slug=product_slug)
    if cart_item:
        cart_item.delete()
        
    return redirect(request.META['HTTP_REFERER'])