from django.contrib import admin
from .models import Customer, Item, \
        Order


admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
