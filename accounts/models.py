from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    pass

USER_TYPE = [
    ("therapist", "I am a Therapist"),
    ("client", "I am Client"),
    ("trainee", "I am a Trainee"),
]


class UserStatus(models.Model):
    """account type ans status"""
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30,default='therapist',choices=USER_TYPE)
    diver = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)

    class Meta:
        permissions = [            
            ("can_dive", "User can access dive section"),            
            ("is_premium", "User have full access of the site"), # not in use
            ("is_therapist", "User can access therapist areas"), # not in use
            ("is_client", "User can access client areas"), # not in use
            ("is_trainee", "User can access trainee areas"), # not in use
           ]


class CommunityProfile(models.Model):
    """profile to display"""
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    about = models.TextField(default='')
    def __str__(self):
        return self.name

REASONS = [
    ("inter", "No interested"),
    ("use", "Interested but not using it"),
    ("no", "No reasons"),
    ("info", "Worried for my privacy"),
    ("fit", "Theory does not fit me"),
]

class DeleteAccount(models.Model):
    """leave trace of deleted accounts"""
    reason = models.CharField(max_length=20, choices=REASONS, default='')
    confirm = models.BooleanField()