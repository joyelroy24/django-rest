from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.permissions import IsStaffPermission
from django.shortcuts import get_object_or_404
from api.authentication import TokenAuthentication
from api.mixins import staffEditorMixin


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'


class ProductlistCreateAPIView(staffEditorMixin,generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # authentication_classes=[authentication.SessionAuthentication,
    #                         TokenAuthentication
    #                         ]
    # permission_classes=[permissions.IsAdminUser,IsStaffPermission]

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        serializer.save()


ProductListCreateapiview=ProductlistCreateAPIView.as_view()#avoid as view on urls.py


class ProductListAPIView(generics.ListAPIView):
    # not used this this is implemented same on create
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        serializer.save()

@api_view(['GET','POST'])
def product_alt_vieW(request,pk=None,*args,**kwargs):
    method=request.method
    if method=='GET':
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        else:
            queryset=Product.objects.all()
            data=ProductSerializer(queryset,many=True).data
            return Response(data)
        
    if method=='POST':
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
        


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'
    def perform_update(self, serializer):
        instance=serializer.save()
        instance.price=222


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    

class productMixinView(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk=kwargs.get('pk')
        if pk!=None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        if pk!=None:
            return self.update(request, *args, **kwargs)
        return self.create(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        print("puttt")
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    
