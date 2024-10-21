from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'   #simplify complex data structure

    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Category name must be greater than 1 character.")
        return value
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price','stock_quantity','image_url', 'created_at', 'category']
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Category name must be greater than 1 character.")
        return value
    def validate_price(self, data):
        if data <= 0.0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return data
    def validate_stock_quantity(self, data):
        if data <= 0:
            raise serializers.ValidationError("We are out of stock.")
        return data
    def create(self, validated_data):
        return Product.objects.create(**validated_data)