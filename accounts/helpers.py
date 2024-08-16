from between_app.models import PersonalStyle
import uuid

def link_session_to_model(request):
    try:
        form_pk = request.session["form_pk"]
        form_pk = uuid.UUID(form_pk)
        form = PersonalStyle.objects.get(pk=form_pk)
        form.user = request.user
        print("form linked to user")
        request.session['linked'] = "true"
    except Exception as e:
        print(f"failed to link user because: {e}")