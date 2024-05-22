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
    """Journal prompts for after a therapy session"""
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
    
class Creation(models.Model):
    """A guided creative process"""
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    #Creation parts
    title = models.CharField(max_length=500, default=None)
    goal = models.CharField(max_length=500, default=None)
    text_sensation = models.TextField(default="")
    text_conection = models.TextField(default="")
    text_metaphore = models.TextField(default="")
    text_concepts = models.TextField(default="")
    text_craft = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'Creations'
    
    def __str__(self):
        """return a string representation of the entry"""
        elipsis = ""
        if len(self.title) >= 50:
            elipsis = "..."
        return f"{self.title[:50]}{elipsis}"
    
class Shadow(models.Model):
    """A guided shadow reflection"""
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    #oposites parts
    title = models.CharField(max_length=500, default=None)
    goal = models.CharField(max_length=500, default=None)
    text_opossite_style = models.TextField(default="")
    text_opposite_sex = models.TextField(default="")
    text_oppossite_elements = models.TextField(default="")
    #wounded healer
    text_transf_characters = models.TextField(default="")
    text_furor_curandis = models.TextField(default="")
    text_trauma_history = models.TextField(default="")
    text_trauma_triggers = models.TextField(default="")
    #plan
    text_care_plan = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'Shadows'
    
    def __str__(self):
        """return a string representation of the entry"""
        elipsis = ""
        if len(self.title) >= 50:
            elipsis = "..."
        return f"{self.title[:50]}{elipsis}"