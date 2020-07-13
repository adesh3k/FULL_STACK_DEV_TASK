from django.db import models
from datetime import datetime
from PIL import Image
# Create your models here.

class Customer(models.Model):
    class Gender(models.TextChoices):
        Male='Male'
        Female='Female'
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=6,choices=Gender.choices,default=Gender.Male)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.now,editable=True)
    image = models.URLField(max_length=300)
    
