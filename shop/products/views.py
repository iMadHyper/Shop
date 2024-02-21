from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from . import models

from django.db.models import Q


categories_template = 'products/categories.html'
products_template = 'products/products.html'


def search(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('query', None)
    
    if query is None:
        return redirect('products:catalog')
    
    products = models.Product.objects.filter(available=True).filter(Q(name__icontains=query) | Q(category__name__icontains=query) | Q(small_description__icontains=query))
    
    on_sale = request.GET.get('on_sale', None)
    order_by = int(request.GET.get('order_by', 1))
    
    if on_sale:
        products = products.filter(discount__gt=0)
        
    if order_by != 1:
        products = products.order_by(order_by_fields[order_by])
    
    paginator = Paginator(products, 3)
    current_page_products = paginator.page(int(page))
    
    context = {
        'products': current_page_products,
        'query' : query
    }
    
    return render(request, products_template, context)

def categories(request):
    categories = models.Category.objects.all()
    
    context = {
        'categories': categories
    }
    
    return render(request, categories_template, context=context)


order_by_fields = {
    2 : "price",
    3 : "-price",
    4 : "-discount"
}

def category_products(request, category_slug):
    
    page = request.GET.get('page', 1)
    
    on_sale = request.GET.get('on_sale', None)
    order_by = int(request.GET.get('order_by', 1))
    
    category = get_object_or_404(models.Category, slug=category_slug)
    products = category.get_available_products()
    
    if on_sale:
        products = products.filter(discount__gt=0)
        
    if order_by != 1:
        products = products.order_by(order_by_fields[order_by])
    
    paginator = Paginator(products, 3)
    current_page_products = paginator.page(int(page))
    
    context = {
        'products': current_page_products
    }
    
    return render(request, products_template, context=context)


def product_detail(request, product_slug):
    pass