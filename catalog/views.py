from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Country,State,City
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.permissions import IsAuthenticated 
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
            
class CountryADD(APIView):
    def post(self, request):
        country_data = request.data
        print(country_data)
        Country.objects.create(**country_data)
        return Response({"message":"Country Add Sucessfully!!!!"})
    def get(self,request):
        countries=Country.objects.values()
        return Response(countries)

class StateADD(APIView):
    def post(self, request):
        state_data = request.data
        print(state_data)
        State.objects.create(**state_data)
        return Response({"message":"State  Add Sucessfully!!!!"})
    def get(self,request):
        state=State.objects.values()
        return Response(state)                         

class cityADD(APIView):
    permission_classes = (IsAuthenticated,)   
    def post(self, request):
        city_data = request.data
        print(city_data)
        City.objects.create(**city_data)
        return Response({"message":"City Add Sucessfully!!!!"})
    def get(self,request):
        city=City.objects.values()
        return Response(city)            