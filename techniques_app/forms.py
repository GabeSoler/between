"""models of the blog forms to add and edit blogs"""
from django import forms 
from .models import Technique


class TechniqueForm(forms.ModelForm):
    class Meta:
        model= Technique
        fields = ("name","component","text","notes","share")
        labels = {"name":"Descriptive name","component":"Related Component(s)","text":"Describe technique","notes":"Add notes to the technique","share":"Make it public?"}
        widgets = {"text":forms.Textarea(attrs={'col':80}),
                   "notes":forms.Textarea(attrs={'col':80})
                   }


