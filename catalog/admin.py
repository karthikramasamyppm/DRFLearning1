from django.contrib import admin

# Register your models here.
from .models import Product,City,Country,State

admin.site.register(Product)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(State)
