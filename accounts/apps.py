from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from allauth.account.signals import user_signed_up, user_logged_in
        from django.dispatch.dispatcher import receiver
        from between_app.models import PersonalStyle
        import uuid

        async def save_user(model,form_pk,user):
            form = model.objects.aget(pk=form_pk)
            form.user = user
            form.save()

        async def save_form_after_log(request,user,model,**kwargs)->str:
            """Base function for adding pk to form after auth"""
            session = request.session
            form_pk = session['form_pk']
            form_pk = uuid.UUID(form_pk)
            linked = session['linked']
            linked = 'processing'
            try:
                await save_user(model,form_pk,user)
            except Exception as e:
                request.session["linked"] = "error"
                error_text = f"failed to link user because: {e}"
                linked = error_text
                print(error_text) # for checking your logs
            else:
                print("form linked to user") # For checking your logs
                linked = "true" #for testing
            return linked

        @receiver(user_signed_up)
        async def user_signed_up(request, user, **kwargs):
            """function to be applied after signup so if there is a test made before it is attached to the user"""
            if request.session["form_pk"]:
                await save_form_after_log(request,user,PersonalStyle,**kwargs)

        @receiver(user_logged_in)
        async def user_logged_in(request, user, **kwargs):
            """function to be applied after login so if there is a test made before it is attached to the user"""
            if request.session["form_pk"]:  
                await save_form_after_log(request,user,PersonalStyle,**kwargs)
        