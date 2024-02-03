from django.contrib import admin
from .models import Product, Category, Review, Order, OrderItem, Cart, CartItem, Address

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Address)

