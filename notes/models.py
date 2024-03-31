from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    tag=models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.tag
    
class Note(models.Model):
    summary=models.CharField(max_length=128, default="Summary")
    text=models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_created"]

    def __str__(self):
        return self.text

