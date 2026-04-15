from django.shortcuts import render
from .models import Card
# Create your views here.

def card_list(request):
    cards = Card.objects.all().select_related('card_type')
    context = {'cards': cards}
    return render(request, 'cards_app/card_list.html',context)