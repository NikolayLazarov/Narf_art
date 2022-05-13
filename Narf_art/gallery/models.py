from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # photo = models.ImageField()
    text = models.CharField(max_length=200)
    pub_date = models.DateField('Date published')
