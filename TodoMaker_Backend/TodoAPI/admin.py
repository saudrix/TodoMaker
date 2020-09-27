from django.contrib import admin

# Register your models here.
from .models import Todo, Item
admin.site.register(Todo)
admin.site.register(Item)

"""
Ajouter les modèles ici permet d'y accèder via l'interface d'administration
D'ajouter de modifier et de retirer des informations de la base
"""
