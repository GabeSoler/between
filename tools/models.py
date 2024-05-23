from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid
from .choices import ATTENDANCE,CLIENT_TYPE
# Create your models here.

class Client(models.Model):
    """a model to organise clients"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    #Client labels
    client_code = models.CharField(default='',max_length=10) #Create a code instead of name
    client_type = models.CharField(default='Pvt',choices=(CLIENT_TYPE),max_length=20) # add choices like private, service, eap, supervisee
    fee = models.IntegerField(default=50,validators=(MinValueValidator(1),MaxValueValidator(100)))
    motive = models.CharField(default='',max_length=200) # what broght them
    rel = models.TextField(default='') # for a relationship description
    goal = models.TextField(default='') # Things you agree to work
    strategy = models.TextField(default='') # what you are thinking you could do


class Session(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    #Session labels
    title = models.CharField(default='Session',max_length=200) #short description
    notes = models.TextField(default='') #longher description
    paid = models.BooleanField(default=False) #check payment
    attended = models.CharField(default='attended',max_length=20,choices=(ATTENDANCE)) #record attendance