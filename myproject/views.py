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
            "Add to Cart": "/api/add-to-cart/",
            "My Cart": "/api/my-cart/",
            "Remove from Cart": "/api/remove-from-cart/",
            "Checkout": "/api/checkout/",
        }
    })