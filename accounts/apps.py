from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from allauth.account.signals import user_signed_up, user_logged_in
        from django.dispatch.dispatcher import receiver
        from between_app.models import PersonalStyle
        import uuid

        def save_form_after_log(request,user,model,**kwargs):
            """Base function for adding pk to form after auth"""
            try:
                form_pk = request.session["form_pk"]
                form_pk = uuid.UUID(form_pk)
                form = model.objects.get(pk=form_pk)
                form.user = user
                form.save()
                print("form linked to user") # For checking your logs
                request.session['linked'] = "true" #for testing
            except Exception as e:
                request.session["form_pk"] = "error"
                error_text = f"failed to link user because: {e}"
                request.session["form_pk_error"] = error_text
                print(error_text) # for checking your logs

        @receiver(user_signed_up)
        def user_signed_up(request, user, **kwargs):
            """function to be applied after signup so if there is a test made before it is attached to the user"""
            save_form_after_log(request,user,PersonalStyle,**kwargs)

        @receiver(user_logged_in)
        def user_logged_in(request, user, **kwargs):
            """function to be applied after login so if there is a test made before it is attached to the user"""
            save_form_after_log(request,user,PersonalStyle,**kwargs)
        