from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to ='image', default = False)
    text = models.CharField(max_length=200)
    pub_date = models.DateField('Date published')

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title