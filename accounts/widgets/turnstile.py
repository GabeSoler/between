from django.forms import Widget,Field
from django.forms.widgets import RadioSelect
from django.core.exceptions import ValidationError
import requests
from urllib.parse import urlencode
from urllib.error import HTTPError
import json
from django.template.loader import render_to_string

class TurnstileWidget(RadioSelect):

    def value_from_datadict(self, data, files, name):
        return data.get('cf-turnstile-response')



class TurnstileField(Field):
    default_error_messages = {
        'error_turnstile': 'Turnstile could not be verified.',
        'invalid_turnstile': 'Turnstile could not be verified.',
        'required': 'Please prove you are a human.',
    }
    def __init__(self, secret_key, site_key):
        self.secret_key = secret_key
        self.site_key = site_key
        self.label="Turnstile"
        self.localize=False,
        self.widget = TurnstileWidget(attrs={"class":"cf-turnstile","data-sitekey":self.site_key})
        super().__init__(widget=self.widget,label=self.label)


    def validate(self,value):
        self.super().validate(value)
        post_data = urlencode({
            'secret': self.secret_key,
            'response': value,
        }).encode()
        try:
            response = requests.post("https://challenges.cloudflare.com/turnstile/v0/siteverify",json=post_data)
        except HTTPError:
            raise ValidationError(self.error_messages['error_turnstile'], code='error_turnstile')

        response_data = json.loads(response.content)

        if not response_data['success']:
            raise ValidationError(self.error_messages['invalid_turnstile'], code='invalid_turnstile')

