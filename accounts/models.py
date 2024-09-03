from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    pass


class UserStatus(models.Model):
    """account type ans status"""
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    therapist = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)

class CommunityProfile(models.Model):
    """profile to display"""
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    about = models.TextField(default='')
    def __str__(self):
        return self.name
    