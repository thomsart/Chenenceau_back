from django.db import models



class ProductCategory(models.Model):
    category = models.CharField(max_length=30, blank=False)
    class Meta:
        ordering = ['category']


class ProductName(models.Model):
    name = models.CharField(max_length=30, blank=False)
    class Meta:
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    manufacturing_cost = models.DecimalField()
    price = models.DecimalField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['category', 'name']