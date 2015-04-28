from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from mixins.forms import UserRegistrationForm

def log_out(request):
    """
    Выход с сайта
    """
    logout(request)
    return redirect('hallway:home')


def log_in(request):
    """
    Вход на сайт
    """
    ctx = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect('hallway:home')
            else:
                ctx.update({'error': 'Ваша учетная запись не активна. За подробностями обращайтесь к администрации сайта.'})
        else:
            ctx.update({'error': 'Неправильный логин или пароль'})
    ctx.update(csrf(request))
    return render_to_response('account/login.html', ctx, context_instance=RequestContext(request))


class RegistrationView(CreateView):
    """
    Регистрация нового пользователя
    """
    form_class = UserRegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('account:login')
