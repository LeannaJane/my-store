from django.urls import path
from .views import (
    CategoryListCreateView, Checkout, ProductListCreateView,
    OrderListCreateView, OrderItemListCreateView,
    AddToCart, RemoveFromCart, MyCartView
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),

    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),

    # Orders
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),

    # Order Items
    path('order-items/', OrderItemListCreateView.as_view(), name='orderitem-list-create'),

    # Add to cart
    path('add-to-cart/<int:product_id>/', AddToCart.as_view(), name='add-to-cart'),

    # My cart
    path('my-cart/', MyCartView.as_view(), name='my-cart'),

    # Remove from cart
    path('remove-from-cart/<int:product_id>/', RemoveFromCart.as_view(), name='remove-from-cart'),

    # Checkout
    path('checkout/', Checkout.as_view(), name='checkout')

]
