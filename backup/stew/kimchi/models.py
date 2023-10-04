from django.db import models
from django.utils import timezone

class textStory(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)