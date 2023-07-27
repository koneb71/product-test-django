from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Product
from app.serializers.products import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'])
    def available(self, request):
        """
        Retrieve a list of all products that are currently available.
        """
        items = Product.objects.filter(status=True)
        serializer = self.get_serializer(items, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def out_of_stock(self, request):
        """
        Retrieve a list of all products that are currently out of stock.
        """
        items = Product.objects.filter(status=False)
        serializer = self.get_serializer(items, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def update_status(self, request, pk=None):
        """
        Update the status of a product to either available or out of stock.
        URL: /api/products/<pk>/update_status/
        Method: PATCH
        """
        product = self.get_object()
        new_status = request.data.get('status')
        if not 'status' in request.data:
            return Response({"error": "Status field is required."}, status=400)

        product.status = new_status
        product.save()

        serializer = self.get_serializer(product)
        return Response(serializer.data)

