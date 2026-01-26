from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from product.models import Product
from .filter import ProductFilter
from .forms import *
from django.contrib.auth import login,logout,authenticate


# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account created successfully')
            return redirect('register')  # Redirect to registration page or login page
        else:
            messages.error(request, 'Please provide correct credentials')
            return render(request, 'user/register.html', {'form': form})

    context = {'form': UserCreationForm()}
    return render(request, 'user/register.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
    
                if user.is_staff:
                    return redirect('admins')  
                else:
                    return redirect('/')   

            else:
                messages.add_message(request, messages.ERROR, "Username or password is invalid")
                return render(request, 'user/loginform.html', {'form': form})
    context = {
        'form': LoginForm()
    }
    return render(request, 'user/loginform.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')


# Homepage view
def homepage(request):
    products = Product.objects.all().order_by('-id')[:8]
    context = {
        'product': products}
    return render(request, 'user/homepage.html', context)


# Product listing page with filters
def productpage(request):
    user = request.user
    products = Product.objects.all().order_by('-id')
    product_filter = ProductFilter(request.GET, queryset=products)
    product_final = product_filter.qs

    context = {
        'product': product_final,
        'product_filter': product_filter,
    }
    return render(request, 'user/productpage.html', context)


# Product detail page
def productdetail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'user/productdetail.html', context)


