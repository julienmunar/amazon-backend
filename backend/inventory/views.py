from pickle import FALSE, TRUE
from re import M
from django.shortcuts import render
from .models import Inventory
from .serializers import InventorySerializer,InventoryUpdateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.




@api_view(['GET','POST'])
# @permission_classes([]) permits to disable authentication for 1 view
@permission_classes([])
def InventoryView(request):

    if request.method == 'GET':
        querySet=Inventory.objects.all()
        serializer=InventorySerializer(querySet,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([])
def InventoryDetailView(request, pk):
    try:
        inventoryDetail=Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print(inventoryDetail)
        serializer=InventorySerializer(inventoryDetail)
        print(serializer.data)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer=InventoryUpdateSerializer(inventoryDetail,data=request.data)
        if serializer.is_valid():          
            serializer.save()
         
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        inventoryDetail.delete()
        return Response(status=status.HTTP_204_BAD_REQUEST)


class InventoryFilter(filters.FilterSet):
    title=filters.CharFilter(lookup_expr='icontains')

class InventoryListView(generics.ListAPIView):
    queryset=Inventory.objects.all()
    serializer_class =InventorySerializer
    filter_backends=[filters.DjangoFilterBackend]
    filterset_fields=['title']
    filterset_class = InventoryFilter

