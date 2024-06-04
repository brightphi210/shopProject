from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import generics
from . models import *
from .serializers import *

# Create your views here.

class ListEndpoint(ListAPIView):
    def get(self, request):
        return Response(
            {'Localhost': 'API DOCS'}, 
        )
    

class ListAndCreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListAndCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer