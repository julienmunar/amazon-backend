from multiprocessing import managers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
from .models import Cart
from .serializers import CartSerializer
from rest_framework.decorators import api_view,permission_classes



@api_view(['GET','POST'])
@permission_classes([])
def CartView(request):

    if request.method == 'GET':
        getCart=Cart.objects.all()
        serializer=CartSerializer(getCart,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=CartSerializer(Cart,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def CartView_detail(request,pk):
    try:
        cart=Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=CartSerializer(cart)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer=CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)