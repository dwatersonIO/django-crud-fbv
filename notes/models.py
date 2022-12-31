from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    text=models.CharField(max_length=255)
    type = models.CharField(max_length=128, default="Generic", choices=(
    ('Generic', "Generic"),
    ('Coding', "Coding"),
    ('Bible', "Bible"),
    ('Exercise', "Exercise"),
    ))
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text

