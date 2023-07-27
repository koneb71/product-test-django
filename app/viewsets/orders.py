from rest_framework import viewsets

from app.models import Order
from app.serializers.orders import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Use prefetch_related to fetch the related products and customer for each order in the queryset
        return super().get_queryset().prefetch_related('customer')
