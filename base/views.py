from django.shortcuts import render
from django.views.decorators.vary import vary_on_cookie


@vary_on_cookie
def index(request):
    template = "index.html"
    return render(request, template)
