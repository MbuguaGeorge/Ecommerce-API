from django.contrib import admin
from .models import Cart, Product, Favourite

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)