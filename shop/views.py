from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
def greetings(r):
    return HttpResponse('Добро пожаловать в наш магазин!')
# Create your views here.

def cats(r):
    response = requests.get('https://catfact.ninja/fact').json()
    print(response)
    return HttpResponse(response['fact'])

