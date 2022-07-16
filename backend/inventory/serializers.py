from dataclasses import fields

from pickle import FALSE
from tokenize import Triple
from typing import ItemsView
from unicodedata import category
from rating.serializer import RatingSerializer
from rest_framework import routers, serializers, viewsets
from .models import Inventory
from .models import ItemCategory
from rating.models import Rating






class ItemCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model=ItemCategory
        fields=['id','title']
   

class InventorySerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField()
    category=ItemCategorySerializer(many=False)
    rating=RatingSerializer(many=False)
    class Meta:
        # read_only_fields = ['id']
        model=Inventory
        fields=['id','title','description','price','category',"image","rating"]
    
    def update(self, instance, validated_data):
        instance.model_method()
        print('test jjuju')
        return super().update(instance, validated_data)
    
class InventoryUpdateSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField()
    category=ItemCategorySerializer(many=False)
    rating=RatingSerializer(many=False)
    class Meta:
        # read_only_fields = ['id']
        model=Inventory
        fields=['id','title','description','price','category',"image","rating"]
    def update(self, instance, validated_data):

        # Retrieve Information from Validated_Data
            category=validated_data.pop("category")
            CategoryTitle=category.get('title')
            rating=validated_data.pop('rating')
            ratingId=rating.get('id')
            
          


        # Check if Category already Exists, if Not to Create
            itemCat=ItemCategory.objects.get(title=CategoryTitle)
            print(itemCat)
            if not itemCat :
                ItemCategory.objects.create(title=CategoryTitle)
                
        # Check if Rating Id Exists, if not pull rating
            itemRating=Rating.objects.get(id=ratingId)
            print(itemRating)
            if itemRating:
                itemRating.rate=rating.get('rate')
                itemRating.count=rating.get('count')
                itemRating.save()
            elif not itemRating:
                Rating.objects.create(**rating)

            instance.title=validated_data.get('title',instance.title)
            instance.description=validated_data.get('description',instance.description)
            instance.category=itemCat
            # instance.rating.rate=rating.get('rate')
            # instance.rating.count=rating.get('count')
            instance.price=validated_data.get('price',instance.price)
            instance.image=validated_data.get('image',instance.image)
            instance.save()
          
        
                

           
            return instance
    

    
  
