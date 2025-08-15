from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Order

class Checkout(APIView):
    def post(self, request):
        order = Order.objects.filter(user=request.user, completed=False).first()
        if not order:
            return Response({"error": "No active order"}, status=400)
        order.completed = True
        order.save()
        return Response({"message": "Order completed"})