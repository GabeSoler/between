from django.db import models
from django.contrib.auth import get_user_model

# Tecniques models
COMPONENTS_GROUP = [
    ("subj", "Subjective"),
    ("ext", "Extended Awareness"),
    ("contx", "Contextual"),
    ("cltr", "Culture"),
    ("idty", "Identity"),
]


class Component(models.Model):
    """a topic to group blog posts"""
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200, choices=COMPONENTS_GROUP)
    about = models.TextField(default='')
    def __str__(self):
        return self.text

class Author(models.Model):
    """the name of the author of blog"""
    name = models.CharField(max_length=200)
    about = models.TextField(default='')
    user_info = models.ForeignKey(get_user_model,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Tecnique(models.Model):
    """the blogs you create"""
    name = models.CharField(max_length=200)
    component = models.ManyToManyField(Component,on_delete=models.PROTECT)
    text = models.TextField(default='')
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    date_made = models.DateField(auto_now_add=True)
    share = models.BooleanField(default=False)
    def __str__(self):
        return self.name