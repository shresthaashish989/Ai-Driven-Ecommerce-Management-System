from django.urls import path
from user.views import *


urlpatterns=[

    path('',hompepage, name='homepage'),
    path('products',productpage, name='productpage'),
    path('productdetail/<int:product_id>',productdetail, name='productdetail')
]