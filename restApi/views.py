from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getItems(request):
    return Response({'items': ['item1', 'item2']})


@api_view(['POST'])
def addItem(request):
    return Response({'items': ['item1', 'item2']})