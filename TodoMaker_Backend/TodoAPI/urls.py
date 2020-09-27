from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

"""
Creation d'un router permettant de gérer les différentes routes de l'API
"""
router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)
router.register(r'item', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
