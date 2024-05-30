"""models of the blog forms to add and edit blogs"""
from django import forms 
from .models import Blog,Blog_Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Blog_Topic
        fields = ("text","about")
        labels = {"text":"Topic Name","about":"Topic Description"}

class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ("name","text","topic")
        labels = {"name":'Blog Title',"text":'',"topic":"Blog Topic"}
        widgets = {"text":forms.Textarea(attrs={'col':80})}


