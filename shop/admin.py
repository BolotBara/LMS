from django.contrib import admin
# Register your models here.
from shop.models import Item, Client
admin.site.register(Item)
admin.site.register(Client)