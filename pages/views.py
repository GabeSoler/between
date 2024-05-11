from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class homeView(TemplateView):
    template_name = 'pages/index.html'

class creationView(TemplateView):
    template_name = 'pages/creation.html'
