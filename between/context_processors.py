def dynamic_base(request):
    host = request.get_host().split(":")[0]

    if host.startswith("cards."):
        base = "_base_clean.html"

    elif host.startswith("profile."):
        base = "_base_clean.html"
    else:
        base = "_base.html"

    return {"BASE_TEMPLATE": base}
