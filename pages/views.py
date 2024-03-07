from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class homeView(TemplateView):
    template_name = 'pages/home.html'

