from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__category_name', lookup_expr='icontains')  # filters foreign key field

    class Meta:
        model = Product
        fields = ['name', 'category']

