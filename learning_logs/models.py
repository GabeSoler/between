from django.db import models
from django.contrib.auth import get_user_model

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        """return a string to represent the model"""
        return self.text
    
class Entry(models.Model):
    """something specific learned abotu a topic"""
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
        