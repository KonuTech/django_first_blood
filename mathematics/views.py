from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request, name="World!"):
    return HttpResponse(f"Hello {name}")