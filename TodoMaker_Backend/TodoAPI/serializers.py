from rest_framework import serializers
from .models import Todo,Item

"""
Classe permettant de transformer automatiquement
les données de json à python à la BDD
"""

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'name')

    def create(self, data):
        return Todo.objects.create(**data)

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)

        instance.save()
        return instance

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('descp','status','id','todo_id')

    def create(self, data):
        return Item.objects.create(**data)
