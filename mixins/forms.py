from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import DateInput

from hallway.models import Suggestion
from forum.models import Answer
from account.models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=40, min_length=4, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=40, min_length=4, required=True)


    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_active = False
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


class UserProfileUpdateForm(UserChangeForm):
    first_name = forms.CharField(label='Имя', max_length=40, min_length=4, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=40, min_length=4, required=True)
    room_number = forms.IntegerField(label='Номер комнаты', required=True)
    dr = forms.DateField(label='Дата рождения', required=True, widget=DateInput)
    is_free = forms.BooleanField(label='Ищу вторую половинку', required=True)

    def save(self, commit=True):
        user = super(UserProfileUpdateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.profile.dr = self.cleaned_data["dr"]
        user.profile.room_number = self.cleaned_data["room_number"]
        user.profile.is_free = self.cleaned_data["is_free"]
        user.is_active = False
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("first_name", "last_name", "dr", "room_number", "is_free")



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['text']