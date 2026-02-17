from django.urls import path
from user.views import *


urlpatterns=[

    path('',homepage, name='homepage'),
    path('about/',aboutpage, name='about'),
    path('product/',productpage, name='productpage'),
    path('productdetail/<int:product_id>',productdetail, name='productdetail'),
    path('register/',register, name='register'),
    path('login/',login_user, name='login'),
    path('logout',logout_view, name='logout'),
    path('add_to_cart/<int:product_id>',add_to_cart,name='add_to_cart'),
    path('cart',cart_list,name='cart_list'),
    path('remove/<int:cart_id>/', deletecartlist, name='remove'),
    path('order/<int:product_id>/<int:cart_id>/', orderitems, name="order"),
    path('myorder',orderlist, name='myorder'),


]