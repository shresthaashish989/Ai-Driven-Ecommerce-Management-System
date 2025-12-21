from django.shortcuts import render
from product.views import *

# Create your views here.


def homepage(request):
    return render(request,'admins/homepage.html')


def productlist(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'admins/productlist.html',context)

def categorylist(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'admins/categorylist.html',context)
