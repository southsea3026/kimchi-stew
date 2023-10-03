from django.db import models

# Create your models here.

class StoryDb(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content

