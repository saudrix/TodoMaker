from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import TodoSerializer, ItemSerializer
from .models import Todo, Item


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()#.order_by('name')
    serializer_class = TodoSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
