from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    product = Product.objects.all()
    print("shammas")
    print(product)
    return render(request, "index.html",{"products":product})