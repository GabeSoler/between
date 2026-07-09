from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def corner_card(card, corner: str):
    return render_to_string("cards_app/_corner.html", {"card": card, "corner": corner})
