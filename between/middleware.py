class SubdomainMiddleware:
    """Routes by subdomain to make parts more clean"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(":")[0]

        if host.startswith("cards."):
            request.urlconf = "cards_app.urls"

        elif host.startswith("profile."):
            request.urlconf = "between_app.urls"

        return self.get_response(request)
