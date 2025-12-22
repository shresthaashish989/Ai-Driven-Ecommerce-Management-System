from django.shortcuts import render,redirect
from product.views import *
from product.forms import *
from django.contrib import messages

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



def addproduct(request):
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"product is succesfully added")
            return redirect('addproduct')
        else:
            messages.add_message(request,messages.ERROR,("Error occured while adding the product"))
            return render(request,'admins/addproduct.html',{'from':form})
    form={
        "form":ProductForm
    }
    return render(request,"admins/addproduct.html",form)
