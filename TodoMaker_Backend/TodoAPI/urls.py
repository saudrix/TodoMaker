from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)
router.register(r'item', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
