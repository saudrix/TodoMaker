from rest_framework import serializers

from .models import Todo,Item

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

    #todo_id = TodoSerializer()
    #todo_id = serializers.IntegerField()
    #id = serializers.IntegerField(read_only=True)
    #descp = serializers.CharField(max_length=200)
    #status = serializers.BooleanField(default=True)

    def create(self, data):
        return Item.objects.create(**data)
