from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class indexView(TemplateView):
    template_name = 'pages/index.html'

class introView(TemplateView):
    template_name = 'pages/intro.html'

class creationView(TemplateView):
    template_name = 'pages/creation.html'

class ProfilesView(TemplateView):
    template_name = 'pages/profiles.html'

class HistoryView(TemplateView):
    template_name = 'pages/history.html'

class ComponentsView(TemplateView):
    template_name = 'pages/components/components.html'