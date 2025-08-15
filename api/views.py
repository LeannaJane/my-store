from rest_framework import generics
from .models import Category, Product, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class AddToCart(APIView):
    def post(self, request, product_id):
        print(request.data)
        product = Product.objects.get(id=product_id)

        # {"quantity": 2}
        order = Order.objects.filter(user=request.user, completed=False).first()

        if order is None:
            order = Order.objects.create(user=request.user, completed=False)
        
        order_item = OrderItem.objects.filter(order=order, product=product).first()
        if order_item is None:
            order_item = OrderItem.objects.create(order=order, product=product)

        order_item.quantity += 1
        order_item.save()
        return Response({"message": f"Added {product.name} to cart"})
    

class MyCartView(APIView):
    def get(self, request):
        order = Order.objects.filter(user=request.user, completed=False).first()
        if not order:
            return Response({"cart": []})
        items = [{"product": item.product.name, "quantity": item.quantity} for item in order.items.all()]
        return Response({"cart": items})
    
class RemoveFromCart(APIView):
    def post(self, request, product_id):
        order = Order.objects.filter(user=request.user, completed=False).first()
        if not order:
            return Response({"error": "No active cart"}, status=400)
        order_item = order.items.filter(product_id=product_id).first()
        if not order_item:
            return Response({"error": "Item not in cart"}, status=400)
        order_item.delete()
        return Response({"message": "Item removed"})
    
class Checkout(APIView):
    def post(self, request):
        order = Order.objects.filter(user=request.user, completed=False).first()
        if not order:
            return Response({"error": "No active order"}, status=400)
        order.completed = True
        order.save()
        return Response({"message": "Order completed"})