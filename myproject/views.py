from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Welcome to the shopping API",
        "endpoints": {
            "Categories": "/api/categories/",
            "Products": "/api/products/",
            "Orders": "/api/orders/",
            "Order Items": "/api/order-items/",
            "Add to Cart": "/api/add-to-cart/<product_id>/",
            "My Cart": "/api/my-cart/",
            "Remove from Cart": "/api/remove-from-cart/<product_id>/",
            "Checkout": "/api/checkout/",
        }
    })