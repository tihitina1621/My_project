from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from .filters import ProductFilter
#from django.contrib.auth.decorators import login_required

#@login_required
class CategoryViewSet(viewsets.ModelViewSet):   #the viewset enables to perform full CRUD functionality
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
#@login_required
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]  #filters a product name and support partial matches
    filterset_class = ProductFilter
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer     #filters a product by category, since the category is a foriegn key
    filter_backends = [filters.SearchFilter]    #http://yourdomain.com/books/?category=some_category, this is how filtering done on browther
    filterset_class = ProductFilter
