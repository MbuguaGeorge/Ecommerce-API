from django.contrib import admin
from .models import Cart, Product, Favourite, New_Arrival

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
admin.site.register(New_Arrival)