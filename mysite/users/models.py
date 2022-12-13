from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    d = datetime.date(1997, 10, 19)
    email = models.EmailField(unique=True)
    dob = models.DateField(default=d)
    profile_picture = models.ImageField(default='default.png',upload_to='uploads/')
    
    

    def __str__(self):
        return self.username
