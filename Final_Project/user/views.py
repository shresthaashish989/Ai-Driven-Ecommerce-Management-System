from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from product.models import *
from .filter import ProductFilter
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


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


def aboutpage(request):
    return render(request,'user/about.html')


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

@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    check_items = Cart.objects.filter(user=user, product=product)

    if check_items.exists():
        messages.add_message(request, messages.ERROR, 'product is already in cart')
        return redirect('productpage')
    else:
        items = Cart.objects.create(user=user, product=product)
        messages.add_message(request, messages.SUCCESS, "Added Product Successfully in Cart")
        return redirect('/productpage')


@login_required
def cart_list(request):
    user=request.user
    items=Cart.objects.filter(user=user)
    data={
        'items':items
    }
    return render(request,'user/cart.html',data)


def deletecartlist(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('cart_list')


def orderitems(request, product_id, cart_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(id=cart_id, user=user)

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            quantity = cart.quantity
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            payment_method = form.cleaned_data['payment_method']

            price = product.price
            total_price = quantity * price

            order = Order.objects.create(
                user=user,
                product=product,
                quantity=quantity,
                total_price=total_price,
                address=address,
                email=email,
                payment_method=payment_method,
                contact=contact,
            )

           
            if payment_method.lower().strip() == "cash on delivery":
                cart.delete()
                messages.success(request, "Order has been successfully placed. Be ready with cash.")
                return redirect("cart_list")

            elif payment_method.lower().strip() == "esewa":
                pass

            elif payment_method.lower().strip() == "khalti":
                pass

            else:
                messages.error(request, f"Invalid payment option: {payment_method}")

    else:
        form = OrderForm()

    return render(request, 'user/orderform.html', {'form': form})




@login_required
def orderlist(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    data={
        'orders':orders
    }
    return render(request,'user/myorder.html',data)


