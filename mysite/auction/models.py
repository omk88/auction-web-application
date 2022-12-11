import os
from django.db import models
from django.conf import settings
#from mysite.users.models import models

def image_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Item(models.Model): 
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=600, default='', blank=True)
    item_image = models.FilePathField(path=image_path)
    end_datetime = models.DateTimeField()
    def __str__(self):
        return "{self.title}, {self.description}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    items = models.ForeignKey(Item)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.amount
