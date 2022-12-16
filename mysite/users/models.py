from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    d = datetime.date(1997, 10, 19)
    email = models.EmailField(unique=True)
    dob = models.DateField(default=d)
<<<<<<< HEAD
    profile_picture = models.ImageField(default='default.png',upload_to='uploads/')
    city = models.CharField(default="London",max_length=150)
=======
    profile_picture = models.ImageField(default='default.png',upload_to='auction/frontend/public/')
>>>>>>> 9583c16d (Modified registration)

    def __str__(self):
        return self.username
    
    def to_dict(self):
        return {
            'email': self.email,
            'dob': self.dob,
            'profile_picture': self.profile_picture.url
        }
