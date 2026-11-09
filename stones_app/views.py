from django.shortcuts import render


def sandbox(request):
    # Pass host status (e.g., staff/admin or room owner is host)
    # is_host = request.user.is_staff
    is_host = True
    return render(request, "stones_app/index.html", {"is_host": is_host})
