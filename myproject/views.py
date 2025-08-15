from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Welcome to the shopping API",
        "endpoints": {
            "products": "/api/product/"
        }
    })