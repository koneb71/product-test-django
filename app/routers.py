from rest_framework.routers import DefaultRouter

from app.viewsets.customers import CustomerViewSet
from app.viewsets.orders import OrderViewSet
from app.viewsets.products import ProductViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customers")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'orders', OrderViewSet, basename="orders")
