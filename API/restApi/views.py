from django.shortcuts import render
from  rest_framework.decorators import api_view
from  rest_framework.response import Response
from .models import Item
from restApi.serializers import ItemSerializer

# Create your views here.
@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def updateItem(request, pk):
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteItem(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response('Item deleted')