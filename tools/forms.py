from django import forms 
from .models import Client,Session




class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_code','client_type','fee','motive','rel','goal','strategy']
        labels = {'client_code':'Add a code identifier for your clients',
                  'client_type':'Chose a client type',
                  'fee':'Agreed fee','motive':'Clients motive for consulting',
                  'rel':'Relational context of client',
                  'goal':'Agreed goal for therapy',
                  'strategy':'Your thoughts for how to approach the process'}
        widgets = {'rel':forms.Textarea(attrs={'cols':80}),
                   'goal':forms.Textarea(attrs={'cols':80}),
                   'strategy':forms.Textarea(attrs={'cols':80})}


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title','notes','paid','attended']
        labels = {'title':'Give an overall title to the session',
                  'notes':'Brief and descriptive note of session',
                  'paid':'Confirm payment',
                  'attended':'Record attendance'}
        widgets = {'notes':forms.Textarea(attrs={'cols':80})}
