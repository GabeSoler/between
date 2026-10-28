import hashlib
import random

from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers

from .models import Card, CardType

# Create your views here.


@login_required(login_url="/accounts/login/")
def card_list(request):
    cards = Card.objects.all().select_related("card_type").order_by("card_type")
    context = {"cards": cards}
    return render(request, "cards_app/card_list.html", context)


def select_card_type_view(request, type_pk=None):
    """For seeing all cards of one type. Its not part of the game like view"""
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


def card_game_view(request, type_pk=None):
    """for the game view, selecting cards and displaying the card types
    adding cache control and vary, so the page can render quickly"""
    template = "cards_app/card_game.html"
    if request.htmx:
        card_group_qs = Card.objects.filter(card_type=type_pk)
        # cache settings
        card_group_list = cache_qs(card_group_qs, 300)
        # random card
        random_card = random.choice(card_group_list)
        template = "cards_app/_card.html"  # this card has an extra link
        context = {"card": random_card, "type": type_pk}
        return render(request, template, context)
    card_type_qs = CardType.objects.all().order_by("name")
    # chaching types
    card_type_list = cache_qs(card_type_qs, 300)
    types = {object.name.lower(): object for object in card_type_list}
    return render(request, template, types)


def cache_qs(queryset, timeout=300):
    model_label = queryset.model._meta.label
    sql, params = queryset.query.sql_with_params()
    cache_key = f"query_cache:{model_label}:{hashlib.md5(f'{sql}:{params}'.encode()).hexdigest()}"
    return_list = cache.get_or_set(cache_key, lambda: list(queryset), timeout=300)
    return return_list
