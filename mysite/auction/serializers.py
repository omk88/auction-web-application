from rest_framework import serializers

from .models import Item, Bid, Question, Answer

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'user',
            'title',
            'starting_price',
            'description',
            'item_image',
            'end_date',
            'end_time'
            ]

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = [
            'id',
            'user',
            'item',
            'amount'
            ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'user',
            'question'
            ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'answer'
            ]