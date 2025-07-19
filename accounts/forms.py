
from .models import CommunityProfile,UserStatus,DeleteAccount
from django import forms
from allauth.account.forms import SignupForm,LoginForm
from accounts.widgets.turnstile import TurnstileField
from decouple import config


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
            'reason':'Please select a reason:',
            'confirm':'Please confirm delete, all your data will be erased.'
        }
        widgets = {
            'reason':forms.RadioSelect,
            'confirm':forms.CheckboxInput,
        }

import sys

class MyCustomSignupForm(SignupForm):
    if 'test' in sys.argv: # I am sending a different form when in testing, to avoid conflicts
        turnstile_field = forms.CharField(max_length=8,required=False)
    else:
        turnstile_field = TurnstileField(secret_key=config('TURNSTILE_SECRET_KEY'),site_key=config('TURNSTILE_SITE_KEY'))

class MyCustomLoginForm(LoginForm):
    if 'test' in sys.argv:
        turnstile_field = forms.CharField(max_length=8,required=False)
    else:
        turnstile_field = TurnstileField(secret_key=config('TURNSTILE_SECRET_KEY'),site_key=config('TURNSTILE_SITE_KEY'))
