from rest_framework import viewsets

from .models import Product

from .serializers import ProductSerializer

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'