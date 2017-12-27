import django
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        available_settings = dir(settings)
        if 'LOGIN_URL' not in available_settings:
            raise Exception('LOGIN_URL must be defined at settings')
        login_url = settings.LOGIN_URL

        if 'LOGIN_EXEMPT_URLS' not in available_settings:
            login_exempt_urls = []
        else:
            login_exempt_urls = settings.LOGIN_EXEMPT_URLS
        login_exempt_urls.append(login_url)

        # Django v2 now has request.user.is_authenticated as a boolean instead
        #       of a function that returns a boolean
        if django.VERSION[0] == 2:
            is_authenticated = request.user.is_authenticated
        else:
            is_authenticated = request.user.is_authenticated()

        # No need to process URLs if user already logged in
        if is_authenticated:
            return self.get_response(request)
        # Let user go through exempt urls
        elif request.path in login_exempt_urls:
            return self.get_response(request)
        # Direct to login URL is user is not authenticated
        else:
            return HttpResponseRedirect(login_url)
