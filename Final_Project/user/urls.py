from django.urls import path
from user.views import *


urlpatterns=[

    path('',homepage, name='homepage'),
    path('products',productpage, name='productpage'),
    path('productdetail/<int:product_id>',productdetail, name='productdetail'),
    path('register/',register, name='register'),
    path('login/',login_user, name='login'),
    path('logout',logout_view, name='logout')
   

]