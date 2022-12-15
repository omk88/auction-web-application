from django.urls import path
from .views import items_api, item_api, search_api, bid_api, question_api, answer_api

urlpatterns = [
    path('api/items/', items_api),
    path('api/item/<int:item_id>/', item_api),
    path('api/search/', search_api),
    path('api/bid/', bid_api),
    path('api/question/', question_api),
    path('api/answer/', answer_api),
]