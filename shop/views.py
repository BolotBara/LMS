from django.shortcuts import render
from django.http import HttpResponse
import requests

from shop.models import Item


def greetings(r):
    return HttpResponse('Добро пожаловать в наш магазин!')
# Create your views here.

def cats(r):
    response = requests.get('https://catfact.ninja/fact').json()
    print(response)
    return HttpResponse(response['fact'])

# def list_item(r):
#     if r.method == "GET"
#     item = Item.objects.all()


def list_item(request):
    queryset = Item.objects.all()
    return render(request, 'list_item.html', context={'all_items': queryset})


def detail_item(request, pk, *args, **kwargs):
    item = Item.objects.get(pk=pk)
    return render(request, 'detail_item.html', context={'item': item})


