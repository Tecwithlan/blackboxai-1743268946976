from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    BUSINESS_TYPES = [
        ('CONTRACTOR', 'Contractor'),
        ('SUPPLIER', 'Supplier'),
        ('WHOLESALER', 'Wholesaler'),
        ('RETAILER', 'Retailer'),
    ]
    
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    tax_exempt = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.business_name} ({self.get_business_type_display()})"
