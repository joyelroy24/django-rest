from rest_framework import viewsets,mixins

from .models import Product

from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

class ProductGenericViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

produt_list_view=ProductGenericViewSet.as_view({'get':'list'})
produt_detailed_view=ProductGenericViewSet.as_view({'get':'retrieve'})
