from rest_framework import routers, serializers, viewsets
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model=Rating
        fields=['id','rate','count']