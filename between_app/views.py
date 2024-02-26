from django.shortcuts import render
from .models import Personal_Style
from django.views.generic import ListView, DetailView,TemplateView,CreateView
from .forms import StyleForm

# Create your views here.

class index_View(TemplateView):
    template_name = 'index.html'

class takeTestView(CreateView):
    model = Personal_Style
    form = StyleForm
    template_name = 'profile_test'
    success_url = '/form_list/'

class resultsList(ListView):
    model = Personal_Style
    context_object_name = 'style_list'

class formDetailView(DetailView):
    model = Personal_Style
    context_object_name = 'style_detail'



class resultsView(DetailView):
    model = Personal_Style
    template_name = 'results.html'
    context_object_name = 'results'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        style = Personal_Style.objects.get(pk=self.kwargs['pk'])
        style = style.cal_Style
        context["style"] = style["compassionate"]
        return context

    

    

    