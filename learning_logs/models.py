from django.db import models
from django.contrib.auth import get_user_model
import uuid

class Topic(models.Model):
    """A topic the user is learning about"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        """return a string to represent the model"""
        return self.text
    
class Entry(models.Model):
    """something specific learned abotu a topic"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """return a string representation of the entry"""
        elipsis = ""
        if len(self.text) >= 50:
            elipsis = "..."
        return f"{self.text[:50]}{elipsis}"

class AfterJournal(models.Model):
    """A log of reflections after therapy sessions"""
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=500, default=None)
    text = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Journals'
    
    def __str__(self):
        """return a string representation of the entry"""
        elipsis = ""
        if len(self.text) >= 50:
            elipsis = "..."
        return f"{self.text[:50]}{elipsis}"