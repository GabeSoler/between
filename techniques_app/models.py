from django.db import models
from django.contrib.auth import get_user_model
import uuid

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



class Technique(models.Model):
    """the blogs you create"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    component = models.ManyToManyField(Component)
    text = models.TextField(default='')
    notes = models.TextField(default='')
    date_made = models.DateField(auto_now_add=True)
    share = models.BooleanField(default=False)
    def __str__(self):
        return self.name