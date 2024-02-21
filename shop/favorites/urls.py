from django.urls import re_path
from . import views


app_name = 'favorites'
urlpatterns = [
    re_path(r"^favorites_change/(?P<product_slug>[-\w]+)/$", views.favorites_change, name='favorites_change'),
    re_path(r"^$", views.favorites, name='favorites'),
]