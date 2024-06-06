from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint, name='localhost'),
    path('products/', views.ListAndCreateProduct.as_view(), name='products'),
    path('product/update/<str:pk>/', views.ListUpdateDeleteProduct.as_view(), name='singleproducts'),
    path('category/', views.ListAndCreateCategory.as_view(), name='category'),
    path('orderitems/', views.ListAndCreateOrderItem.as_view(), name='orderitems'),
    path('orders/', views.ListAndCreateOrder.as_view(), name='order'),
    path('order/update/<str:pk>/', views.ListUpdateDeleteOrder.as_view(), name='order'),
]