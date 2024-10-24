from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from allauth.account.signals import user_signed_up, user_logged_in
        from django.dispatch.dispatcher import receiver
        from between_app.models import PersonalStyle
        import uuid
        from django.contrib import messages

        def save_user(model,form_pk,user):
            form = model.objects.get(pk=form_pk)
            form.user = user
            form.save()

        def save_form_after_log(request,user,model,**kwargs)->str:
            """Base function for adding pk to form after auth"""
            try:
                form_pk = request.session['form_pk']
                form_pk = uuid.UUID(form_pk)
                save_user(model,form_pk,user)
            except Exception as e:
                error_text = f"Failed to link test to user because: {e}"
                messages.error(request,error_text) # for checking your logs
            else:
                messages.info(request,"Form linked to user") # For checking your logs
                request.session['linked'] = "true"

        @receiver(user_signed_up)
        def user_signed_up(request, user, **kwargs):
            """function to be applied after signup so if there is a test made before it is attached to the user"""
            if 'form_pk' in request.session:
                save_form_after_log(request,user,PersonalStyle,**kwargs)

        @receiver(user_logged_in)
        def user_logged_in(request, user, **kwargs):
            """function to be applied after login so if there is a test made before it is attached to the user"""
            if 'form_pk' in request.session:
                save_form_after_log(request,user,PersonalStyle,**kwargs)
        