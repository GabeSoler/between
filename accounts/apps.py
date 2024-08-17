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
        def user_signed_up(request, user, **kwargs):
            """function to be applied after signup so if there is a test made before it is attached to the user"""
            try:
                form_pk = request.session["form_pk"]
                form_pk = uuid.UUID(form_pk)
                form = PersonalStyle.objects.get(pk=form_pk)
                form.user = user
                form.save()
                print("form linked to user")
                request.session['linked'] = "true" #for testing
            except Exception as e:
                print(f"failed to link user because: {e}")

        @receiver(user_logged_in)
        def user_logged_in(request, user, **kwargs):
            """function to be applied after login so if there is a test made before it is attached to the user"""
            try:
                form_pk = request.session["form_pk"]
                form_pk = uuid.UUID(form_pk)
                form = PersonalStyle.objects.get(pk=form_pk)
                form.user = user
                form.save()
                print("form linked to user")
                request.session['linked'] = "true" #for testing
            except Exception as e:
                print(f"failed to link user because: {e}")
        