from django.shortcuts import render, redirect, get_object_or_404

from .models import FavoriteItem
from products.models import Product


favorites_template = 'favorites/favorites.html'

def favorites(request):
    if request.user.is_authenticated:
        favorites = FavoriteItem.objects.filter(user=request.user)
    else:
        favorites = FavoriteItem.objects.filter(session_key=request.session.session_key)
        
    context = {
        'favorites' : favorites
    }
        
    return render(request, favorites_template, context)

def favorites_change(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    if request.user.is_authenticated:
        favorite, created = FavoriteItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            favorite.delete()
    else:
        favorite, created = FavoriteItem.objects.get_or_create(session_key=request.session.session_key, product=product)
        if not created:
            favorite.delete()
            
    return redirect(request.META['HTTP_REFERER'])