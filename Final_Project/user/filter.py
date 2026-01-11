import django_filters
from django_filters import CharFilter
from product.models import Product

class ProductFilter(django_filters.FilterSet):
    product_name_contains = CharFilter(field_name='name', lookup_expr='icontains', label='')

    class Meta:
        model = Product
        fields = []
        exclude = ['category', 'description', 'price', 'stock', 'image', 'created_at', 'updated_at', 'available']
