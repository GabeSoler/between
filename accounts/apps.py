from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from allauth.account.signals import user_signed_up, user_logged_in
        from django.dispatch.dispatcher import receiver
        from between_app.models import PersonalStyle
        import uuid

        @receiver(user_signed_up)
        def user_signed_up(request, **kwargs):
            try:
                form_pk = request.session["form_pk"]
                form_pk = uuid.UUID(form_pk)
                form = PersonalStyle.objects.get(pk=form_pk)
                form.user = request.user
                print("form linked to user")
                request.session['linked'] = "true"
            except Exception as e:
                print(f"failed to link user because: {e}")

        @receiver(user_logged_in)
        def user_logged_in(request, **kwargs):
            try:
                form_pk = request.session["form_pk"]
                form_pk = uuid.UUID(form_pk)
                form = PersonalStyle.objects.get(pk=form_pk)
                form.user = request.user
                print("form linked to user")
                request.session['linked'] = "true"
            except Exception as e:
                print(f"failed to link user because: {e}")
        