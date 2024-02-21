from django.urls import re_path
from . import views


app_name = 'products'
urlpatterns = [
    re_path(r"^catalog/(?P<category_slug>[-\w]+)/$", views.category_products , name="category_products"),
    re_path(r"^product/(?P<product_slug>[-\w]+)/$", views.product_detail , name="product_detail"),
    re_path(r"^catalog/", views.categories, name='catalog'),
    re_path(r"^$", views.search, name='search'),
]