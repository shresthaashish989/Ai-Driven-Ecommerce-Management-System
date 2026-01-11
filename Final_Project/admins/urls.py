from django.urls import path
from .views import *


urlpatterns=[
    path('admins',homepage, name='admins'),
    path('productlist/',productlist, name='productlist'),
    path('categorylist/',categorylist, name='categorylist'),
    path('addproduct/',addproduct, name='addproduct'),
    path('addcategory/',addcategory, name='addcategory'),
    path('updateproduct/<int:product_id>',updateproduct, name='updateproduct'),
    path('deleteproduct/<int:product_id>',deleteproduct, name='deleteproduct'),
    path('updatecategory/<int:category_id>',updatecategory, name='updatecategory'),
    path('deletecategory/<int:category_id>',deletecategory, name='deletecategory'),
]