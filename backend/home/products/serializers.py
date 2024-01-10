from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    url=serializers.SerializerMethodField(read_only=True)
    urlhyper=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    class Meta:
        model=Product
     
        fields=['urlhyper','url','pk','title','content','sale_price','my_discount']

    def get_url(self,obj):
        request=self.context.get('request')
        if request is None:
            return None
    
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request) 

    def get_my_discount(self,obj):

        if not hasattr(obj,'id'):#check the object is saved in product database if it exist it have id attribute otherwise it's not saved so just reurn none
            return None
        if not isinstance(obj,Product):#check the object is an instance of product
            return None
            
        else:
            return obj.get_discount()