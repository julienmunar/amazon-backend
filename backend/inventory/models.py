from distutils.command.upload import upload
from django.db import models

from rating.models import Rating

# Create your models here.


class ItemCategory(models.Model):
    title=models.CharField(max_length=30,null=True)

    def __str__(self): 
            return self.title



class Inventory(models.Model):
    title=models.CharField(max_length=30,unique=True)
    description=models.TextField()
    price=models.FloatField(max_length=4)
    category=models.ForeignKey(ItemCategory,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to="upload",null=True,blank=True)
    rating=models.ForeignKey(Rating,related_name="ratingInvent", on_delete=models.CASCADE)


    def __str__(self):
        return self.title