from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_home(request,*args,**kwargs):
    data={}
    print("body below")
    print(request.body)
    try:
        print(type(request.body)) #class byte
        # data=request.body.decode('utf-8')
        # print(data)
        # print(type(data))
        data=json.loads(request.body) #convert to dictionary format
        print("Loadssss")
        print(data)
        print(type(data))  
        
    except json.JSONDecodeError as e:
        print(e)

    print(print(type(request.headers)))
    print(dict(request.headers))
    data['header']=dict(request.headers)
    data['content_type']=request.content_type
    
    data['get_parameter']=request.GET
    return JsonResponse(data)