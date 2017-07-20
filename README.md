# django-login-required
A Django Middleware to protect all URLs behind a login

### Installation
1. Install using pip:

    pip install django-login-required

1. Include the middleware in your settings.py after the AuthenticationMiddleware:

    MIDDLEWARE = [
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'login_required.middleware.LoginRequiredMiddleware',
        ...
    ]

1. Specify the settings for LOGIN_URL and (optionally) LOGIN_EXEMPT_URLS:

    LOGIN_URL = "/login/"
    LOGIN_EXEMPT_URLS = [
        # LOGIN_URL is always exempt, no need to repeat it here
        "/password_reset/",
        "/password_reset/done/"
    ]

And you should be good to go!

### Credits    
These links helped me arrive at this solution:

[Stackoverflow question](https://stackoverflow.com/questions/2164069/best-way-to-make-djangos-login-required-the-default)

[One Creative Blog](http://onecreativeblog.com/post/59051248/django-login-required-middleware)

### License

MIT License
