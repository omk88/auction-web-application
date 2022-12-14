from django.urls import path
from .views import items_api, item_api, search_api

urlpatterns = [
    path('api/items/', items_api),
    path('api/item/<int:item_id>/', item_api),
    path('api/search/', search_api),
]