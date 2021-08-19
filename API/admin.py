from django.contrib import admin
from .models import Cart,Product, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)