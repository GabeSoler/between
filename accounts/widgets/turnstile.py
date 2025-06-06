from django.forms import Widget,Field
from django.core.exceptions import ValidationError
import requests
from urllib.parse import urlencode
from urllib.error import HTTPError
import json
from between.settings import DEBUG

class TurnstileWidget(Widget):

    def __init__(self, site_key):
        super().__init__()
        self.site_key = site_key
        self.attrs = {"class":"cf-turnstile",'data-sitekey':self.site_key}

    
    def get_context(self, name, value, attrs):
        return {
            "turnstile": {
                "name": name,
                "is_hidden": self.is_hidden,
                "value": self.format_value(value),
                "attrs": self.build_attrs(self.attrs, attrs),
                "template_name":'turnstile/turnstile.html',
            },
        }

    def value_from_datadict(self, data, files, name):
        return data.get('cf-turnstile-response')

    @property
    def is_hidden(self):
        return self.input_type == "hidden" if DEBUG == False else ""


class TurnstileField(Field):
    default_error_messages = {
        'error_turnstile': 'Turnstile could not be verified.',
        'invalid_turnstile': 'Turnstile could not be verified.',
        'required': 'Please prove you are a human.',
    }

    def __init__(self, secret_key, site_key, help_text=None, disabled=False):
        super().__init__(help_text=help_text, disabled=disabled)
        self.secret_key = secret_key
        self.site_key = site_key
        self.required=True
        self.label=""
        self.help_text = help_text
        self.disabled = disabled
        widget = TurnstileWidget(site_key)
        widget.is_required = self.required


    def validate(self,value):
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

