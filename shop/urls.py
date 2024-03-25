from django.urls import path

from shop.views import greetings, cats, list_item, detail_item

urlpatterns = [
    path('greeting/', greetings),
    path('facts/', cats),
    path('', list_item),
    path('<int:pk>/', detail_item)
]

# http://127.0.0.1:8000/shop/1/