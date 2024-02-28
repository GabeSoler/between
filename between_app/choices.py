from django.db import models
from django.utils.translation import gettext_lazy as _


class Response_Choices(models.IntegerChoices):
    reject = -5, _("I feel contrary")
    ok     = 1, _("It sound ok?")
    little = 3,_("I feel a little close to it")
    agree = 6,_("I agree with the premise")
    main = 10,_("I feel it is my style")


