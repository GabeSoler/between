import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Card, CardType

# Create your views here.


@login_required(login_url="/accounts/login/")
def card_list(request):
    cards = Card.objects.all().select_related("card_type").order_by("card_type")
    context = {"cards": cards}
    return render(request, "cards_app/card_list.html", context)


def select_card_type_view(request, type_pk=None):
    template = "cards_app/card_types.html"
    if request.htmx:
        card_group = Card.objects.filter(card_type=type_pk)
        random_card = random.choice(card_group)
        template = "cards_app/hx_card.html"  # this card has an extra link
        context = {"card": random_card, "type": type_pk}
        return render(request, template, context)
    card_type = CardType.objects.all().order_by("name")
    context = {"types": card_type}
    return render(request, template, context)

