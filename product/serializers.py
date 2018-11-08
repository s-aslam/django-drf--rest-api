from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    discription = serializers.CharField(required=True)
    unit = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ('name','discription', 'unit','price')     
