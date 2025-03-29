from django.db import models
from django.core.validators import MinValueValidator

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Product Categories"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    UNIT_CHOICES = [
        ('EA', 'Each'),
        ('PK', 'Pack'),
        ('BX', 'Box'),
        ('PL', 'Pallet'),
        ('LB', 'Pound'),
    ]
    
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='EA')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    min_order_quantity = models.PositiveIntegerField(default=1)
    current_stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.sku} - {self.name}"

class BulkPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bulk_prices')
    min_quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        ordering = ['min_quantity']
        unique_together = ['product', 'min_quantity']
    
    def __str__(self):
        return f"{self.product.name} - {self.min_quantity}+: ${self.price}"
