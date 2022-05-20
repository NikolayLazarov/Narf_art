from django import forms
from .models import Card

from .models import Image

class CardForm (forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name','author','photo','text','pub_date')




class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')