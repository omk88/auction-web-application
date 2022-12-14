import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import Q

from .models import Item
from .serializers import ItemSerializer

@csrf_exempt
def items_api(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse({
            'items': serializer.data
        })

@csrf_exempt
def item_api(request: HttpRequest, item_id: int) -> HttpResponse:
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item, many=False)
    if request.method == 'GET':
        return JsonResponse({
            'item': serializer.data
        })
    if request.method == 'DELETE':
        item.delete()
        return JsonResponse({'message': 'Item was deleted'})

@csrf_exempt
def search_api(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        item_text = data[0]
        items = Item.objects.filter(Q(title__icontains=item_text) | Q(description__icontains=item_text))
        serializer = ItemSerializer(items, many=True)
        return JsonResponse({
            'items': serializer.data
        })

