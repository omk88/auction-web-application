import os
from django.db import models
from django.conf import settings
from users.models import models

def image_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Item(models.Model): 
    user = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=600, default='', blank=True)
    item_image = models.FilePathField(path=image_path)
    end_datetime = models.DateTimeField()

    def __str__(self):
        return "{self.title}, {self.description}"

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'title': self.title,
            'starting_price': self.starting_price,
            'description': self.description,
            'item_image': self.item_image,
            'end_datetime': self.end_datetime
        }

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='bids', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='bids', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.amount
    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'item': self.item,
            'amount': self.amount
        }

class Comment(models.Model):
    user = models.ForeignKey(User)
    comment = description = models.TextField(max_length=600, default='', blank=True)

    def __str__(self):
        return self.comment

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'comment': self.comment,
        }