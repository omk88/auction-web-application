from django.urls import path
from .views import items_api, item_api

urlpatterns = [
    #path('', index),
    path('api/items/', items_api),
    path('api/item/<int:item_id>/', item_api),
]