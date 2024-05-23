from django.shortcuts import render

# Create your views here.

def index(request):
    """show all tools"""
    return render(request,'tools/index.html')
