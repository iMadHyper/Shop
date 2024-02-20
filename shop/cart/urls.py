from django.urls import re_path
from . import views


app_name = 'cart'
urlpatterns = [
    re_path(r"^cart_add/(?P<product_slug>[-\w]+)/$", views.cart_add, name='cart_add'),
    re_path(r"^cart_change/(?P<product_slug>[-\w]+)/$", views.cart_change, name='cart_change'),
    re_path(r"^cart_remove/(?P<product_slug>[-\w]+)/$", views.cart_remove, name='cart_remove'),
    re_path(r"^$", views.cart, name='cart'),
]