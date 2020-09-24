from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)
    descp = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.descp
