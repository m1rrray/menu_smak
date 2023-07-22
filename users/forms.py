from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django.core.exceptions import ValidationError
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from .models import User, Address


class CreationForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input__text'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input__text'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("phone", "first_name", "last_name", "password1", 'password2',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input__text'}),
            'last_name': forms.TextInput(attrs={'class': 'input__text'}),
            'phone': forms.TextInput(attrs={'class': 'input__text'}),
            'password1': forms.PasswordInput(attrs={'class': 'input__text'}),
            'password2': forms.PasswordInput(attrs={'class': 'input__text'}),
        }


class LoginUserForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input__text'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'input__text'}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(phone)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields["phone"].max_length = username_max_length
        self.fields["phone"].widget.attrs["maxlength"] = username_max_length
        if self.fields["phone"].label is None:
            self.fields["phone"].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        phone = self.cleaned_data.get("phone")
        password = self.cleaned_data.get("password")

        if phone is not None and password:
            self.user_cache = authenticate(
                self.request, phone=phone, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"phone": self.username_field.verbose_name},
        )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'apartment_number']

        widgets = {
            'street': forms.TextInput(attrs={'class': 'input__text'}),
            'apartment_number': forms.TextInput(attrs={'class': 'input__text'})
        }


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', "last_name", 'phone')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input__text'}),
            'last_name': forms.TextInput(attrs={'class': 'input__text'}),
            'phone': forms.TextInput(attrs={'class': 'input__text'}),

        }

