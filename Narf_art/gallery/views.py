from django.http import HttpResponse
from django.shortcuts import render

from .models import Card

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"index.html")

# def get_by_name(request, )
def card_by_id(request,card_id):
    card = Card.objects.get(pk = card_id)
    # cards = Card.objects.all()
    return render(request,'index.html', {'card': card })
    # return render(request,'index.html', {'card': cards })

    # return HttpResponse(f"Card: {card.name}, published by {card.author}")

def all_cards(request):
    # card = Card.objects.get(pk = card_id)
    cards = Card.objects.all()
    # return render(request,'index.html', {'card': card })
    return render(request,'all_cards.html', {'cards': cards })

    # return HttpResponse(f"Card: {card.name}, published by {card.author}")

def probe(request):
    cards = Card.objects.all()
    # return render(request,'index.html', {'card': card })
    return render(request,'probe.html', {'cards': cards })