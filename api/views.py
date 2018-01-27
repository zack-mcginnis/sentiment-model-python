from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls index.")
