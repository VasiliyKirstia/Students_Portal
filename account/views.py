from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin, FormView
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def log_in(request):
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
                    return redirect('forum:home')
            else:
                ctx.update({'error': 'Пользователь отключён'})
        else:
            ctx.update({'error': 'Неправильный логин или пароль'})
    ctx.update(csrf(request))
    return render_to_response('account/login.html', ctx, context_instance=RequestContext(request))


def log_out(request):
    logout(request)
    return redirect('forum:home')


#TODO убрать костыль и сделать нормально
class RegistrationUser(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'email', 'password']
    template_name = 'account/registration.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        try:
            #Эта штука должна регистрировать нового пользователя, но она регистрирует недопользователя без пароля
            User.objects.create_user(form.username, email=form.email,
                                     password=form.password,
                                     first_name=form.first_name,
                                     last_name=form.last_name)
        except:
            pass
        return super(RegistrationUser, self).form_valid(form)