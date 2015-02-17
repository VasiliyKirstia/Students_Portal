from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django import forms

from forum.models import *


class UserCreationFormExtended(UserCreationForm):
    first_name = forms.CharField(max_length=40, label='Имя', required=True)
    last_name = forms.CharField(max_length=40, label='Фимилия', required=True)


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationFormExtended, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


def log_out(request):
    logout(request)
    return redirect('forum:home')


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


class RegistrationView(CreateView):
    form_class = UserCreationFormExtended
    template_name = 'account/registration.html'
    success_url = reverse_lazy('hallway:home')
