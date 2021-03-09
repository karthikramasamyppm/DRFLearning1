from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.HelloWorldView.as_view(), name="hello"),
    path('product/', views.productDetail, name="product"),
    path('productview/', views.ProductView.as_view(), name="product1"),
    path('productadd/', views.ProductADD.as_view(), name="productadd"),
    
]


