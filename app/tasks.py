from celery import shared_task
from app.models import Product
from app.utils import confirm_order_email


@shared_task
def process_order_data(payload):
    for item in payload['items']:
        product = Product.objects.filter(sku=item['sku']).first()
        product.quantity = product.quantity - item['quantity']
        item['name'] = product.name
        product.save()

    confirm_order_email(payload)
