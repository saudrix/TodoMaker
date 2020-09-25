from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template import loader
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from rest_framework import viewsets

from .serializers import TodoSerializer, ItemSerializer
from .models import Todo, Item

from rest_framework.decorators import api_view

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
#class TodoViewSet(viewsets.ModelViewSet):

    #permissions_classes = (permissions.IsAuthenticated,)
    #serializer_class = MyModelleSerializer

    #@api_view(['GET', 'POST', 'DELETE'])
    #def TodoViewSet(request):
    #    if request.method == 'GET':

    #        queryset = Todo.objects.all()#.order_by('name')
    #        serializer_class = TodoSerializer(queryset, many=True)
    #        return JsonResponse(serializer_class.data, safe=False)

"""
factory = APIRequestFactory()
request = factory.get('/')

serializer_context = {
    'request': Request(request),
}
"""

"""
class TodoView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)#, context = serializer_context)
        return Response({'todos':serializer.data})

    def get(self, request, pk):
        todos = get_object_or_404(Todo.objects.all(), pk=pk)
        serializer = TodoSerializer(todos, many=True)
        return Response({'todos':serializer.data})


    def post(self, request):
        todo = request.data.get('todo')

        # Create an article from the above data
        serializer = TodoSerializer(data=todo)
        if serializer.is_valid(raise_exception=True):
            todo_saved = serializer.save()
        return Response({"success": "New todo '{}' created successfully".format(todo_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Todo.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Todo with id `{}` has been deleted.".format(pk)},status=204)
"""

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()#.order_by('name')
    #serializer_class = TodoSerializer
    serializer_class = TodoSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()#.order_by('name')
    #serializer_class = TodoSerializer
    serializer_class = ItemSerializer



class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True, context={'request': request})
        return Response({'items':serializer.data})

    def post(self, request):
        item = request.data.get('item')

        # Create an article from the above data
        serializer = ItemSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "New item '{}' created successfully".format(item_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Item.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Item with id `{}` has been deleted.".format(pk)},status=204)

    def put(self, request, pk):
        saved_item = get_object_or_404(Item.objects.all(), pk=pk)
        data = request.data.get('item')
        serializer = ItemSerializer(instance=saved_item, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "Item '{}' updated successfully".format(item_saved.name)})
