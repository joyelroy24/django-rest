from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request,*args,**kwargs):
    data={}

    # instance=Product.objects.all().order_by("?").first()
    # if instance:
    #     data=ProductSerializer(instance).data
    
    # print("body below")
    # print(request.body)
    # try:
    #     print(type(request.body)) #class byte
    #     # data=request.body.decode('utf-8')
    #     # print(data)
    #     # print(type(data))
    #     data=json.loads(request.body) #convert to dictionary format
    #     print("Loadssss")
    #     print(data)
    #     print(type(data))  
        
    # except json.JSONDecodeError as e:
    #     print(e)

    # print(print(type(request.headers)))
    # print(dict(request.headers))
    # data['header']=dict(request.headers)
    # data['content_type']=request.content_type
    
    # data['get_parameter']=request.GET


    #inject data
    data=request.data
    serializer=ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):#return more correct response  like validate like required filed missing.
        print("^^")
        print(serializer.validated_data)
        instance=serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({"invalid":'Not good Data'},status=400)

