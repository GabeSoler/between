from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def stone(type_number):
    return render_to_string("stones_app/_stone.html", {"type_number": type_number})
