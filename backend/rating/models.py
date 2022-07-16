from django.db import models

# Create your models here.

class Rating(models.Model):
    rate=models.FloatField(max_length=1,null=True)
    count=models.IntegerField(null=True)


    def __str__(self):
        return "Rate:{}---Count:{}".format(self.rate,self.count)