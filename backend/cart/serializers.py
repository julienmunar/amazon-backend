from rest_framework import routers, serializers, viewsets
from .models import Cart,SelectedProduct
from myUser.models import MyUser

class SelectedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=SelectedProduct
        fields="__all__"

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["firstname", "lastname", "email"]

class CartSerializer(serializers.ModelSerializer):
    products=SelectedProductSerializer(many=True)
    user=userSerializer()
    class Meta:
        model=Cart
        fields="__all__"