# myproject/urls.py (app-level)
from django.urls import path
from api.views import Checkout, RemoveFromCart
from .views import AddToCart, CategoryListCreateView, MyCartView, OrderItemListCreateView, OrderListCreateView, ProductListCreateView, register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Login
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Register
    path('register/', register_user, name='register'),

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
    path('checkout/', Checkout.as_view(), name='checkout'),


]
