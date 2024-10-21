from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'   #simplify complex data structure
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price','stock_quantity','image_url', 'created_at', 'category']
    def validate(self, data):
        if len(data['name']) < 2:
            raise serializers.ValidationError("Name must be at least 5 characters long.")
        return data
    def validate(self, data):
        if data['price'] <= 0.0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return data
    def validate(self, data):
        if data['stock_quantity'] <= 0:
            raise serializers.ValidationError("We are out of stock.")
        return data
    