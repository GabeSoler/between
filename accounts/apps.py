from django.apps import AppConfig
from django.dispatch.dispatcher import receiver




class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from allauth.account.signals import user_signed_up
        from between_app.models import PersonalStyle

        @receiver(user_signed_up, dispatch_uid="unique")
        def user_signed_up(request, user, **kwargs):
            form_pk = request.session.get("form_pk")
            form = PersonalStyle.objects.get(pk=form_pk)
            form.user = request.user
