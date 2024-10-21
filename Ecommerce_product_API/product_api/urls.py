from django.urls import path, include
from . import views
from .views import ProductViewSet, CategoryViewSet, ProductListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Catagories', CategoryViewSet, basename='category')
router.register(r'Products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListView.as_view(), name='product_list'),
    #path('product-list/', ProductViewSet.as_view({'get': 'list'}), name='product_list'),
    #path('category-viewset/', CategoryViewSet.as_view({'get': 'list'}), name='category-viewset'),
]