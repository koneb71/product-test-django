from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'price', 'description', 'quantity',
            'status', 'created_at', 'updated_at'
        ]
