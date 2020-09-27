from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template import loader
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

from .serializers import TodoSerializer, ItemSerializer
from .models import Todo, Item

from rest_framework.decorators import api_view

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
# Create your views here.
"""
Ici on créer les vues qui vont être utilisées pour le display de data
"""

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()#.order_by('name')
    #serializer_class = TodoSerializer
    serializer_class = TodoSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()#.order_by('name')
    #serializer_class = TodoSerializer
    serializer_class = ItemSerializer
