from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListEndpoint.as_view(), name='views'),
    path('products/', views.ListAndCreateProduct.as_view(), name='views'),
    path('category/', views.ListAndCreateCategory.as_view(), name='views')
]