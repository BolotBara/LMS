from django.contrib import admin
# Register your models here.
from shop.models import Item, Client, Purchase

admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Purchase)
