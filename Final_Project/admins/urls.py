from django.urls import path
from .views import *


urlpatterns=[
    path('admins',homepage, name='admins'),
    path('productlist/',productlist, name='productlist'),
    path('categorylist/',categorylist, name='categorylist'),
    path('addproduct/',addproduct, name='addproduct'),
]