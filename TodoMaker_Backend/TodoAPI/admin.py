from django.contrib import admin

# Register your models here.
from .models import List
from .models import Item

admin.site.register(List)
admin.site.register(Item)
