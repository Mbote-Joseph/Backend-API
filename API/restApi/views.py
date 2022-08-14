from django.shortcuts import render
from  rest_framework.decorators import api_view
from  rest_framework.response import Response
from .models import Item,Book
from restApi.serializers import ItemSerializer, BookSerializer

# Create your views here.
# Getting Items
@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# Posting Item
@api_view(['POST'])
def postItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# Updating Item
@api_view(['PUT'])
def updateItem(request, pk):
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# Deleting Item
@api_view(['DELETE'])
def deleteItem(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response('Item deleted')



# Books API
@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def updateBook(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)