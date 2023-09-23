from django.db import models

class StoryDb(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Total(models.Model):
    score = models.IntegerField()