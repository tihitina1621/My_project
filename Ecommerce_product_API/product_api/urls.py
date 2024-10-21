from django.urls import path, include
from . import views
from .views import ProductViewSet, CategoryViewSet, ProductListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Catagory', CategoryViewSet, basename='category')
router.register(r'Product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListView.as_view(), name='product_list'),
]