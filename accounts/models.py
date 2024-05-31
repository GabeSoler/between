from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass


class UserStatus(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    therapist = models.BooleanField(default=True)
    client = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)

class CommunityProfile(models.Model):
    """the name of the author of blog"""
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    about = models.TextField(default='')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    