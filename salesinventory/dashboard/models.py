from django.db import models
from django.utils import timezone

# Category models here.
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
# Products models here.
class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=255)
    cat_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

# Products models here.
class Sales(models.Model):
    id = models.BigAutoField(primary_key=True)
    caty_name = models.CharField(max_length=100)
    s_product = models.CharField(max_length=100)
    s_price = models.CharField(max_length=255)
    s_quantity = models.CharField(max_length=255)
    s_total = models.CharField(max_length=255)
    s_created_at = models.DateField(default=timezone.now)
    
class adminlogin(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    