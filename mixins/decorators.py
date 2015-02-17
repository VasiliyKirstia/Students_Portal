from django.contrib.auth.decorators import login_required


def login_required_for_class(cls):
    origin = cls.as_view
    modified = lambda *args, **kwargs: login_required(origin(*args, **kwargs))
    cls.as_view = modified
    return cls