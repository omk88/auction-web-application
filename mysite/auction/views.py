from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Item

# Create your views here.

def items_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict() 
                for item in Item.objects.all()
            ]
        })
    
def item_api(request: HttpRequest, item_id: int) -> HttpResponse:
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'GET':
        return JsonResponse(item.to_dict())
    if request.method == 'DELETE':
        item.delete()
        return JsonResponse({'message': 'Item was deleted'})

