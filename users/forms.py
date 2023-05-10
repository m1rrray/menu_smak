import phonenumber_field
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import NewUser
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CreationForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input__text'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input__text'}))

    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = ("fullname","username", "phone", "email", "password1", 'password2',)

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'input__text'}),
            'phone': forms.TextInput(attrs={'class': 'input__text'}),
            'email': forms.EmailInput(attrs={'class': 'input__text'}),
            'password1': forms.PasswordInput(attrs={'class': 'input__text'}),
            'password2': forms.PasswordInput(attrs={'class': 'input__text'}),
            'username': forms.TextInput(attrs={'class': 'input__text'}),
        }


class LoginUserForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input__text', }))
    # username = forms.CharField(widget=forms.TextInput(attr={'class':'input__text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input__text'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'input__text'}))

    widgets = {
        'username': forms.TextInput(attrs={'class': 'input__text'}),
    }