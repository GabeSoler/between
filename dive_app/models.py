from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.



class Creation(models.Model):
    """A guided creative process"""
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    #Creation parts
    title = models.CharField(max_length=500, default=None)
    goal = models.CharField(max_length=500, default=None)
    text_sensation = models.TextField(default="",blank=True,null=True)
    text_conection = models.TextField(default="",blank=True,null=True)
    text_metaphore = models.TextField(default="",blank=True,null=True)
    text_concepts = models.TextField(default="",blank=True,null=True)
    text_craft = models.TextField(default="",blank=True,null=True)

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
    text_opossite_style = models.TextField(default="",blank=True,null=True)
    text_opposite_sex = models.TextField(default="",blank=True,null=True)
    text_oppossite_elements = models.TextField(default="",blank=True,null=True)
    #wounded healer
    text_transf_characters = models.TextField(default="",blank=True,null=True)
    text_furor_curandis = models.TextField(default="",blank=True,null=True)
    text_trauma_history = models.TextField(default="",blank=True,null=True)
    text_trauma_triggers = models.TextField(default="",blank=True,null=True)
    #plan
    text_care_plan = models.TextField(default="",blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Shadows'
    
    def __str__(self):
        """return a string representation of the entry"""
        elipsis = ""
        if len(self.title) >= 50:
            elipsis = "..."
        return f"{self.title[:50]}{elipsis}"