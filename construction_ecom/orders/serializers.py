from rest_framework import serializers
from products.serializers import ProductSerializer
from users.serializers import UserSerializer
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'bulk_price', 'line_total']
        read_only_fields = ['unit_price', 'bulk_price', 'line_total']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date', 'status', 'tax_exempt',
                 'tax_rate', 'subtotal', 'tax_amount', 'total', 'notes', 'items']
        read_only_fields = ['order_date', 'subtotal', 'tax_amount', 'total']

    def create(self, validated_data):
        # Custom logic for order creation will be added here
        pass