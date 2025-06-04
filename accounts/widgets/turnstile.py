from django.forms import Widget,Field
from django.core.exceptions import ValidationError
from decouple import config

class TurnstileWidget(Widget):
    def __init__(self,site_key,attrs=None):
        self.attrs = {} if attrs is None else attrs.copy()
        self.site_key = site_key
        self.template_name = 'widget/turnstile.html'


    
    def get_context(self, name, value, attrs):
        return {
            "widget": {
                "name": name,
                "is_hidden": self.is_hidden,
                "required": self.is_required,
                "value": self.format_value(value),
                "attrs": self.build_attrs(self.attrs, attrs),
                "template_name": self.template_name,
                "key":self.site_key,
            },
        }


class TurnstileField(Field):
    widget = TurnstileWidget()  # Default widget to use when rendering this type of Field.
    hidden_widget = (
        widget  # Default widget to use when rendering this as "hidden".
    )
    default_validators = []  # Default set of validators
    # Add an 'invalid' entry to default_error_message if you want a specific
    # field error message not raised by the field validators.


TURNSTILE_SECRET_KEY = config('TURNSTILE_SECRET_KEY')

def validate_turnstile(value):
    ...


# someone solverd in github, checking their validators
# they send a url request to the address with the two info, not the ip... but added a proxy option
# zmh-program/django-turnstile
