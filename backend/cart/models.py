from tkinter import N
from turtle import ondrag
from django.db import models
from inventory.models import Inventory
from myUser.models import MyUser
from django.utils import timezone


class SelectedProduct(models.Model):
    product_FK=models.ForeignKey(Inventory, related_name="product_selected", on_delete=models.CASCADE)
    quantity=models.IntegerField( blank=True,null=True)


# Create your models here.
class Cart(models.Model):
    title=models.CharField(max_length=60, null=True)
    user=models.ForeignKey(MyUser, related_name="cartUser", on_delete=models.CASCADE)
    date=models.DateTimeField(verbose_name="Cart Date",default=timezone.now)
    products=models.ManyToManyField(SelectedProduct, related_name="CartList",blank=True,null=True)

    def __str__(self):
        return (f"{self.user} - {self.date}")

  