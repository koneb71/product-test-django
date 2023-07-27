from rest_framework import viewsets

from app.models import Customer
from app.serializers.customers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
