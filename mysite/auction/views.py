from django.shortcuts import render
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

