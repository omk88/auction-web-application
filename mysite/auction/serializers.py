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