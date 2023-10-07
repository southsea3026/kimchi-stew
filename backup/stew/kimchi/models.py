from django.db import models
from django.utils import timezone

class textStory(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    block = models.CharField(max_length=255, default='default_value')