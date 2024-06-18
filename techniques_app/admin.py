from django.contrib import admin
from techniques_app.models import Technique,Component,TechSaved

# Register your models here.



admin.site.register(Technique)
admin.site.register(Component)
admin.site.register(TechSaved)