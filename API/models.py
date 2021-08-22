from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

SHOES = 'shoes'
CLOTHES = 'clothes'
ACCESSORIES = 'accessories'

CATEGORY = (
    (SHOES,'shoes'),
    (CLOTHES,'clothes'),
    (ACCESSORIES,'accessories')
)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(choices=CATEGORY,max_length=100,default=SHOES)
    product_price = models.FloatField()
    thumbnail = models.ImageField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.OneToOneField(User, models.CASCADE, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username