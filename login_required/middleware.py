from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # No need to process URLs if user already logged in
        if request.user.is_authenticated():
            return self.get_response(request)
        elif request.path in ["/login/", "/password_reset/", "/password_reset/done/"]:
            return self.get_response(request)
        else:
            return HttpResponseRedirect("/login")
