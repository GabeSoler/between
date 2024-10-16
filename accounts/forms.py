
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CommunityProfile,UserStatus,DeleteAccount
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

class CommunityProfileForm(forms.ModelForm):
    """ Form to display information in the techniques app """
    class Meta:    
        model = CommunityProfile
        fields = ('name','about')
        labels = {
            "name":"Your community name (it can be a nickname)",
            "about":"About to display (so others know a bit about you)"
        }

class UserStatusForm(forms.ModelForm):
    """Form for describing user types"""
    class Meta:    
        model = UserStatus
        fields = ('therapist','diver')
        labels = {
            "therapist":"I am a therapist (or trainee)? (for reference)",
            "diver":"Become a Diver (full access)"
        }
        widgets = {
            'therapist':forms.CheckboxInput,
            'dive':forms.CheckboxInput,
        }

class DeleteAccountForm(forms.ModelForm):
    """a form before deleting account"""
    class Meta:
        model = DeleteAccount
        fields = ('reason','confirm')
        labels = {
            'reason':'Please select a reason',
            'confirm':'Please confirm delete, all your data will be erased'
        }
        widgets = {
            'reason':forms.RadioSelect,
            'confirm':forms.CheckboxInput,
        }
        