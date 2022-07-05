from django.db import models

from users.models import User



class ProductCategory(models.Model):
    category = models.CharField(max_length=30, blank=False, unique=True)
    class Meta:
        ordering = ['category']


class ProductName(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    class Meta:
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    manufacturing_cost = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['category', 'name']
        unique_together = ['category', 'name']


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        ordering = ['user', '-created']
        unique_together = ['user', 'product']


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        ordering = ['user', '-created']
