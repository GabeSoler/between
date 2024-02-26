from django.db import models
from django.utils.translation import gettext_lazy as _


class Response_Choices(models.IntegerChoices):
    reject = -1, _("I reject")
    little = 1,_("I feel a little close")
    agree = 3,_("I agree")
    main = 7,_("I feel commited")


