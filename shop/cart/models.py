from django.db import models

from users.models import User
from products.models import Product


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart_item.products_price() for cart_item in self)
    
    def total_sell_price(self):
        return sum(cart_item.products_sell_price() for cart_item in self)
    
    def total_quantity(self):
        if self:
            return sum(cart_item.quantity for cart_item in self)
        return 0


class CartItem(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'cart_item'
        
    objects = CartQuerySet().as_manager()
    
    def products_price(self):
        return self.product.price * self.quantity
    
    def products_sell_price(self):
        return self.product.get_sell_price() * self.quantity
    
    def __str__(self):
        if self.user:
            return f'{self.user.username} | {self.product.name} | {self.quantity} | {self.created_timestamp}'