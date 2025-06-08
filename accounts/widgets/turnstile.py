from django.forms import Field
from django.forms.widgets import CheckboxInput
from django.core.exceptions import ValidationError
import requests
from urllib.parse import urlencode
from urllib.error import HTTPError
import json


class TurnstileWidget(CheckboxInput):
    template_name = 'accounts/widgets/turnstile.html'
    def __init__(self, site_key,attrs=None):
        self.site_key = site_key
        super().__init__(attrs=attrs)

    def value_from_datadict(self, data, files, name):
        return data.get('cf-turnstile-response')


    def get_context(self, name, value, attrs):
       context = super().get_context(name, value, attrs)
       context['widget']['key'] = self.site_key
       context['key'] = self.site_key
       context['attrs']['key'] = self.site_key
       return context

#todo find out the right place of the key and erase the rest, make async the check, and test.
class TurnstileField(Field):
    default_error_messages = {
        'error_turnstile': 'Turnstile could not be verified.',
        'invalid_turnstile': 'Turnstile could not be verified.',
        'required': 'Please prove you are a human.',
    }
    def __init__(self, secret_key, site_key):
        self.secret_key = secret_key
        self.site_key = site_key
        self.widget = TurnstileWidget(site_key=site_key,attrs={'key':self.site_key})
        super().__init__()


    def validate(self,value):
        super().validate(value)
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

    def super(self):
        pass

