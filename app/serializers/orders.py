from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Order, Customer, Product
from app.serializers.customers import CustomerSerializer
from app.tasks import process_order_data


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('items')
        customer_data = validated_data.pop('customer')

        customer, _ = Customer.objects.get_or_create(**customer_data)

        for product_data in products_data:
            product = Product.objects.filter(sku=product_data['sku']).first()
            if not product:
                raise ValidationError(f"SKU: {product_data['sku']} not found.")

            if not product.quantity or not product.status:
                raise ValidationError(f"SKU: {product_data['sku']} is out of stock.")

            if product_data['quantity'] > product.quantity:
                raise ValidationError(f"SKU: {product_data['sku']}. Ordered quantity is greater than product's remaining stock.")

        order = Order.objects.create(customer=customer, items=products_data, **validated_data)
        order.save()

        payload = dict(
            items=products_data,
            order_number=validated_data['order_number'],
            created_at=order.created_at.strftime('%Y-%m-%d %H:%M'),
            customer_name=customer.name,
            customer_email=customer.email,
        )
        process_order_data.delay(payload)
        return order
