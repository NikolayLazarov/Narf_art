from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect

from .models import Card
from .forms import CardForm

# from .forms import ImageForm

from django.conf import settings

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"index.html")

# def get_by_name(request, )
def card_by_id(request,card_id):
    card = Card.objects.get(pk = card_id)
    # cards = Card.objects.all()
    return render(request,'product.html', {'card': card })
    # return render(request,'index.html', {'card': cards })

    # return HttpResponse(f"Card: {card.name}, published by {card.author}")

def all_cards(request):
    # card = Card.objects.get(pk = card_id)
    cards = Card.objects.all()
    # img = Card.objects.all()
    # return render(request,'index.html', {'card': card })
    return render(request,'all_cards.html', {'cards': cards})

    # return HttpResponse(f"Card: {card.name}, published by {card.author}")

def probe(request):
    cards = Card.objects.all()
    # return render(request,'index.html', {'card': card })
    return render(request,'main.html', {'cards': cards })


# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'main.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'main.html', {'form': form})

def addProduct(request):
    if request.method == "POST":
        new_card = Card()
        new_card.name = request.POST.get("name")
        new_card.author = request.POST.get("author")
        new_card.text = request.POST.get("text")
        new_card.pub_date = request.POST.get("pub_date")
        
        if len(request.FILES) != 0:
           new_card.photo = request.POST.get("photo")
        
        new_card.save()
        messages.success(request, "Product adeded sucessfullu")
        return redirect('/gallery/card')
    return render(request, 'add_card.html')
    
def mainPaige(request):
    return render(request, 'main.html')
def shop(request):
    cards = Card.objects.all()

    return render(request, 'shop.html', {'cards': cards})

def aboutUsPage(request):
    return render(request, 'abouts-uss.html')

def footer(request):
    return render(request, 'FOOTER1.html')
# def image_upload_view(request):
#     """Process images uploaded by users """
#     if request.method == "POST":
#         form = CardForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj':img_obj})
    
#     else:
#         form = CardForm()
#     return render(request, 'main.html',  {'form':form})