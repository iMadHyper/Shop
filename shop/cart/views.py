from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import CartItem
from products.models import Product


cart_template = 'cart/cart_items.html'

def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    
    context = {
        'cart_items' : cart_items
    }
    
    return render(request, cart_template, context)

def cart_add(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart_item, created = CartItem.objects.get_or_create(session_key=request.session.session_key, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            
    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, product_slug):
    cart_item = get_object_or_404(CartItem, user=request.user, product__slug=product_slug)
    cart_item.delete()
        
    return redirect(request.META['HTTP_REFERER'])