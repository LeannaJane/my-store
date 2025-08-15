from rest_framework.generics import ListCreateAPIView
from ..models import Order, OrderItem
from ..serializers import OrderSerializer, OrderItemSerializer

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer