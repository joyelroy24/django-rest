from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'


class ProductlistCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

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