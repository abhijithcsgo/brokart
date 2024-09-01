from django.shortcuts import render
from . import models
# Create your views here.

def show_cart(request):
    return render(request,'cart.html')
