from django.core.management.base import BaseCommand
from django.db import IntegrityError

from app.models import Product

sample_products = [
    {
        'name': 'Product A',
        'sku': 'ABCD1234',
        'price': 19.99,
        'description': 'This is the description of Product A.',
        'quantity': 50,
        'status': True,  # In stock
    },
    {
        'name': 'Product B',
        'sku': 'EFGH5678',
        'price': 12.49,
        'description': 'Product B is a high-quality item.',
        'quantity': 100,
        'status': True,  # In stock
    },
    {
        'name': 'Product C',
        'sku': 'SKU003',
        'price': 29.95,
        'description': 'Product C comes in multiple colors.',
        'quantity': 75,
        'status': True,  # In stock
    },
    {
        'name': 'Product D',
        'sku': 'SKU004',
        'price': 9.99,
        'description': 'Product D is perfect for everyday use.',
        'quantity': 25,
        'status': True,  # In stock
    },
    {
        'name': 'Product E',
        'sku': 'SKU005',
        'price': 39.99,
        'description': 'Product E is a top-notch gadget.',
        'quantity': 60,
        'status': True,  # In stock
    },
    {
        'name': 'Product F',
        'sku': 'SKU006',
        'price': 14.95,
        'description': 'Product F is lightweight and portable.',
        'quantity': 30,
        'status': True,  # In stock
    },
    {
        'name': 'Product G',
        'sku': 'SKU007',
        'price': 49.99,
        'description': 'Product G is made from eco-friendly materials.',
        'quantity': 80,
        'status': True,  # In stock
    },
    {
        'name': 'Product H',
        'sku': 'SKU008',
        'price': 5.99,
        'description': 'Product H is a budget-friendly option.',
        'quantity': 10,
        'status': True,  # In stock
    },
    {
        'name': 'Product I',
        'sku': 'SKU009',
        'price': 89.99,
        'description': 'Product I is a premium item with advanced features.',
        'quantity': 5,
        'status': False,  # Out of stock
    },
    {
        'name': 'Product J',
        'sku': 'SKU010',
        'price': 24.99,
        'description': 'Product J is a bestselling item.',
        'quantity': 150,
        'status': True,  # In stock
    },
]


class Command(BaseCommand):
    help = 'Creates 10 sample products.'

    def handle(self, *args, **kwargs):
        for product_data in sample_products:
            try:
                product = Product.objects.create(**product_data)
                product.save()
            except IntegrityError:
                pass
