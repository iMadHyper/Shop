from django.urls import re_path
from . import views

# re_path(r'^logout/', views.signout, name='logout'),
app_name = 'users'
urlpatterns = [
    re_path(r'^login/', views.login_user, name='login'),
    re_path(r'^signup/', views.signup_user, name='signup'),
    re_path(r'^logout/', views.logout_user, name='logout'),
    re_path(r'^profile/', views.profile, name='profile'),
]