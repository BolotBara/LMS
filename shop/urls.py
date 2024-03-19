from django.contrib import admin
from django.urls import path, include

from shop.views import greetings, cats

urlpatterns = [
    path('greeting/', greetings),
    path('facts/', cats)
]
