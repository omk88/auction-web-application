from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Item
from .serializers import ItemSerializer

# Create your views here.
def items_api(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse({
            'items': serializer.data
        })
    
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

