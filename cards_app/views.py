from django.shortcuts import render

# Create your views here.

def card_list(request):
    return render(request, 'cards_app/cards_list.html')