from email.mime import image
from django.db import DEFAULT_DB_ALIAS, models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Card(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    photo = models.ImageField()
