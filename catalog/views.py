from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"})


@api_view(['GET'])
def productDetail(request):
    tasks={}
    tasks1 = Product.objects.values()
    print(tasks1)
    return Response(tasks)


class ProductView(APIView):
    def get(self, request):
        tasks=[]
        tasks1 = Product.objects.values()
        print(tasks1)
        for s in tasks1:
            print(s)
            tasks.append(s)
        return Response(tasks)

class ProductADD(APIView):
    def post(self, request):
        product_data = request.data
        print(product_data)
        Product.objects.create(**product_data)
        return Response({"message":"Product Add Sucessfully!!!!"})
            