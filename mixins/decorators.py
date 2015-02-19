from django.contrib.auth.decorators import login_required


def login_required_for_class(cls):
    origin = cls.as_view
    modified = lambda *args, **kwargs: login_required(origin(*args, **kwargs))
    cls.as_view = modified
    return cls

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
#from django.views.generic import TemplateView
#
#class ProtectedView(TemplateView):
#    template_name = 'secret.html'
#
#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super(ProtectedView, self).dispatch(*args, **kwargs)