# django-login-required
A Django Middleware to protect all URLs behind a login

### Overview

Django is fantastic. It has anything you might need for your application. Unfortunately, if the majority of your application needs to be protected by a login form, you will need to do this to *all* your views ([source](https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator)):

```
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
```

**OR** ([source](https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-loginrequired-mixin))

```
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
```

Which can be quite painful. What if you look at it in the opposite way? You can make your whole application default to this @login_required/LoginRequiredMixin (sort of), and then tell the application which URLs are safe to be viewed without authentication, for example: the frontpage, the login and password recovery pages, about page, contact form, etc.

That's where this tiny Middleware comes in handy!

### Installation
1. Install using pip:
```
pip install django-login-required
```
1. Include the middleware in your settings.py after the AuthenticationMiddleware:
```
    MIDDLEWARE = [
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'login_required.middleware.LoginRequiredMiddleware',
        ...
    ]
```
1. Specify the settings for LOGIN_URL and (optionally) LOGIN_EXEMPT_URLS:
```
    LOGIN_URL = "/login/"
    LOGIN_EXEMPT_URLS = [
        # LOGIN_URL is always exempt, no need to repeat it here
        "/password_reset/",
        "/password_reset/done/"
    ]
```
And you should be good to go!

### Credits    
These links helped me arrive at this solution:

[Stackoverflow question](https://stackoverflow.com/questions/2164069/best-way-to-make-djangos-login-required-the-default)

[One Creative Blog](http://onecreativeblog.com/post/59051248/django-login-required-middleware)

### License

MIT License

### Changelog

* **v0.2** - Added support for Django 2.0
