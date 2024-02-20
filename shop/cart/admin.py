from django.contrib import admin
from . import models

@admin.register(models.CartItem)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
    ordering = ('user', 'product', 'quantity', 'created_timestamp')