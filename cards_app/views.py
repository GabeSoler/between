from django.shortcuts import render
from .models import Card
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def card_list(request):
    cards = Card.objects.all().select_related('card_type').order_by('card_type')
    context = {'cards': cards}
    return render(request, 'cards_app/card_list.html',context)