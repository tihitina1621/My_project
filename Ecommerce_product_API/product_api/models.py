from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image_url = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

products = Product.objects.prefetch_related('category')
#separate query will be performed 