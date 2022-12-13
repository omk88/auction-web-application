from django.urls import path

from .views import items_api

urlpatterns = [
    #path('', index),
    path('api/items/', items_api),
]