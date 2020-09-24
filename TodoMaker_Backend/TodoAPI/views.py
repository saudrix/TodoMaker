from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ListSerializer, ItemSerializer
from .models import List, Item


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()#.order_by('name')
    serializer_class = ListSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
