import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import Q
from django.conf import settings

from users.models import CustomUser
from .models import Item, Bid, Question, Answer
from .serializers import ItemSerializer, BidSerializer, QuestionSerializer, AnswerSerializer

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

@csrf_exempt
def bid_api(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        current_user = get_object_or_404(CustomUser, id=request.user.id)
        item_data = get_object_or_404(Item, id=data['item'])
        current_bid = Bid.objects.get(Q(item = item_data))
        if (current_bid is None):
            bid = Bid(user = current_user, item = item_data, amount = data['amount'])
            bid.save()
            serializer = BidSerializer(bid, many=False)
            return JsonResponse({
                'bid': serializer.data
            })
        elif (float(data['amount']) > float(current_bid.amount)):
            current_bid.delete()
            bid = Bid(user = current_user, item = item_data, amount = data['amount'])
            bid.save()
            serializer = BidSerializer(bid, many=False)
            return JsonResponse({
                'bid': serializer.data
            })
        else:
            return JsonResponse({'message': 'Invalid bid'})

@csrf_exempt
def question_api(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        current_user = get_object_or_404(CustomUser, id=request.user.id)
        item_data = get_object_or_404(Item, id=data['item'])
        question = Question(user = current_user, item = item_data, question = data['question'])
        question.save()
        serializer = QuestionSerializer(question, many=False)
        return JsonResponse({
            'question': serializer.data
        })

@csrf_exempt
def answer_api(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        current_user = get_object_or_404(CustomUser, id=request.user.id)
        item_data = get_object_or_404(Item, id=data['item'])
        question_data = get_object_or_404(Question, id=data['question'])
        if (item_data.user == current_user):
            answer = Answer(user = current_user, item = item_data, question = question_data, answer = data['answer'])
            answer.save()
            serializer = AnswerSerializer(answer, many=False)
            return JsonResponse({
                'answer': serializer.data
            })
        else:
            return JsonResponse({'message': 'Not the owner'})

@csrf_exempt
def bids_api(request: HttpRequest, item_id: int) -> HttpResponse:
    if request.method == 'GET':
        item_data = get_object_or_404(Item, id=item_id)
        bids = get_object_or_404(Bid, item=item_data)
        serializer = BidSerializer(bids, many=False)
        return JsonResponse({
            'bids': serializer.data
        })

@csrf_exempt
def questions_api(request: HttpRequest, item_id: int) -> HttpResponse:
    if request.method == 'GET':
        item_data = get_object_or_404(Item, id=item_id)
        questions = Question.objects.filter(Q(item=item_data))
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse({
            'questions': serializer.data
        })

@csrf_exempt
def answers_api(request: HttpRequest, question_id: int) -> HttpResponse:
    if request.method == 'GET':
        question_data = get_object_or_404(Question, id=question_id)
        answers = Answer.objects.filter(Q(question=question_data))
        serializer = AnswerSerializer(answers, many=True)
        return JsonResponse({
            'answers': serializer.data
        })
@csrf_exempt
def get_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        current_user = request.user
        return JsonResponse(current_user.id, safe=False)
