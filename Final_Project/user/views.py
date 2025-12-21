from django.shortcuts import render
from product.models import *

# Create your views here.

def hompepage(request):
    product=Product.objects.all()
    items={
        'product':product
    }
    return render(request,'user/homepage.html',items)