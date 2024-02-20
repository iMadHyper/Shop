from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import math


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(verbose_name='Фото', upload_to='categories/', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']
        
        
    def __str__(self):
        return self.name
    
    def get_available_products(self):
        return self.products.filter(available=True)
    
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(verbose_name='Фото', upload_to='manufacturers/', blank=True, null=True)


    class Meta:
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'
        ordering = ['name']

    
    def __str__(self):
        return self.name
    
    def get_available_products(self):
        return self.products.filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products', verbose_name='Производитель', blank=True, null=True)
    name = models.CharField(verbose_name='Название', max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    discount = models.IntegerField(verbose_name='Скидка', default=0)
    image = models.ImageField(verbose_name='Фото', upload_to='products/', blank=True, null=True)
    small_description = models.TextField(verbose_name='Небольшое описание', max_length=250, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    characteristics = models.TextField(verbose_name='Характеристики', blank=True, null=True)
    available = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['name', 'price', '-discount']


    def __str__(self):
        return self.name

    def get_sell_price(self):
        if self.discount:
            return self.price - self.discount
        return self.price