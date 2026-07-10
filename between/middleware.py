"""Routes by subdomain to make parts more clean"""


class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(":")[0]
        if host.startswith("cards."):
            request.urlconf = "between.urls"  # Point to a different urls.py

        return self.get_response(request)
