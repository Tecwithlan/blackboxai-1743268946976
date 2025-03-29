from rest_framework import serializers
from .models import Product, ProductCategory, BulkPrice

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'parent', 'description']

class BulkPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkPrice
        fields = ['id', 'min_quantity', 'price']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    bulk_prices = BulkPriceSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'category', 'description', 
                 'unit', 'base_price', 'min_order_quantity',
                 'current_stock', 'image', 'active', 'bulk_prices']
        extra_kwargs = {
            'image': {'required': False}
        }