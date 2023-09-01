from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # answer_set

class Answer(models.Model):
    option = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)