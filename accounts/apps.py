from django.apps import AppConfig
from django.dispatch.dispatcher import receiver




class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from allauth.account.signals import user_signed_up, user_logged_in
        from between_app.models import PersonalStyle

        @receiver(user_signed_up, dispatch_uid="unique")
        def user_signed_up(request, user, **kwargs):
            try:
                form_pk = request.session("form_pk")
                form = PersonalStyle.objects.get(pk=form_pk)
                form.user = user
            except Exception as e:
                print(e)

        @receiver(user_logged_in, dispatch_uid="unique")
        def user_signed_up(request, user, **kwargs):
            try:
                form_pk = request.session("form_pk")
                form = PersonalStyle.objects.get(pk=form_pk)
                form.user = user
            except Exception as e:
                print(e)