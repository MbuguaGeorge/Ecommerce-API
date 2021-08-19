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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)