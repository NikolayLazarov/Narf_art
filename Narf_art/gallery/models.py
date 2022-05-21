from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to ='image', default = False)
    text = models.TextField()
    pub_date = models.DateField('Date published')
    price = models.IntegerField(blank=True, null=True)