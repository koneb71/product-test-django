from django.contrib import admin

from app.models import Product, Customer, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
