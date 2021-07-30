from django.db import models
from django.contrib.auth.models import User
# Create your models here.

SHOES = 'shoes'
CLOTHES = 'clothes'
ACCESSORIES = 'accessories'

CATEGORY = (
    (SHOES,'shoes'),
    (CLOTHES,'clothes'),
    (ACCESSORIES,'accessories')
)

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(choices=CATEGORY,max_length=100,default=SHOES)
    product_price = models.FloatField()
    thumbnail = models.ImageField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True)