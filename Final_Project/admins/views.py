from django.shortcuts import render,redirect,get_object_or_404
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



def addcategory(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Category is succesfully added")
            return redirect('addcategory/')
        else:
            messages.add_message(request,messages.ERROR,"Error Occur while adding the category")
            return render(request, "admins/addcategory.html",{'form':form})
    forms={
        "form":CategoryForm
    }
    return render(request, 'admins/addcategory.html',forms)



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


def updateproduct(request,product_id):
    instance=Product.objects.get(id=product_id)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES, instance=instance)
        if form.is_valid:
            form.save()
            messages.add_message(request,messages.SUCCESS,"Product is updated succesfully")
            return redirect('productlist')
        else:
            messages.add_message(request,messages.ERROR,"Error occur while adding the product")
            return render(request,'admins/updateproduct.html',{'form':form})
    forms={
        "form":ProductForm(instance=instance)
    }
    return render(request,'admins/updateproduct.html',forms)


def deleteproduct(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,"product is delete succesfully")
    return redirect('productlist/')


def updatecategory(request,category_id):
    instace=Category.objects.get(id=category_id)
    if request.method=="POST":
     form=CategoryForm(request.POST, instance=instace)
     if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS,"category is succefully updated")
         return redirect('categorylist')

     else:
         messages.add_message(request,messages.ERROR,"Error while Update the product")
         return render(request,'admins/updatecategory.html',{"form":form})
    
    forms={
         "form":CategoryForm(instance=instace)
     }
    return render(request,'admins/updatecategory.html',forms)
    
     
    

def deletecategory(request, category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,"category is delete succesfully")
    return redirect('/categorylist/')

   
