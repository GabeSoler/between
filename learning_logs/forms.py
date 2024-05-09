from django import forms 
from .models import Topic,Entry,AfterJournal

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

class AfterForm(forms.ModelForm):
    class Meta:
        model = AfterJournal
        fields = ['question','text']
        labels = {'question':'Add a question','text':'Write a reflective entry'}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}