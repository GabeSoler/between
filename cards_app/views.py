from multiprocessing import context

from django.shortcuts import render
from .models import Card,CardType
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def card_list(request):
    cards = Card.objects.all().select_related('card_type').order_by('card_type')
    context = {'cards': cards}
    return render(request, 'cards_app/card_list.html',context)

def select_card_type__view(request):
    card_type = CardType.objects.all()
    context = {'types':card_type}
    return render(request,'cards_app/card_types.html',context)