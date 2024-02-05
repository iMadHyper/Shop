from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manufacturer', 'price', 'discount', 'available')
    list_filter = ('name', 'category', 'manufacturer', 'price', 'discount', 'available')
    list_editable = ["discount",]

    fields = [
            "name",
            "slug",
            "category",
            "manufacturer",
            ("price", "discount"),
            'available',
            "image",
            'small_description',
            "description",
            'characteristics'
    ]

    search_fields = ('name', 'description', 'characteristics')
    ordering = ('available', 'name')
    
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
    ordering = ('name',)
    
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
    ordering = ('name',)
    
    prepopulated_fields = {"slug": ("name",)}