from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import generics
from . models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def endpoint(request):
    data = {
        'localhost/' : 'List of Endpoint',
        'api/token' : 'Login User',
        'api/refresh' : 'Refresh User Token',
        'products/' : 'To create and get new products',
        'product/update/id/' : 'To update, get, and delete products',
        'category/' : 'To create and get new category',
        'orderItems/' : 'To create and get new Order Items',
        'orders/' : 'To create and get new Orders',
    }

    return Response(data)
    

class ListAndCreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListUpdateDeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ListAndCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListAndCreateOrderItem(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class ListAndCreateOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class ListUpdateDeleteOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'