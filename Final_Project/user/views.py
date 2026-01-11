from django.shortcuts import render
from product.models import *
from .filter import *

# Create your views here.

def hompepage(request):
    product=Product.objects.all()
    items={
        'product':product
    }
    return render(request,'user/homepage.html',items)



def productpage(request):
    user=request.user
    product = Product.objects.all().order_by('-id')
    product_filter=ProductFilter(request.GET, queryset=product)
    product_final=product_filter.qs
    context={
        'product':product_final,
        'product_filter':product_filter,
       

    }
    return render(request,'user/productpage.html',context)



def productdetail(request,product_id):
    product=Product.objects.get(id=product_id)

    data={
        'product':product
    }
    return render(request,'user/productdetail.html',data)