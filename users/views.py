from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import CreationForm, LoginUserForm
from .models import NewUser


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')  # где login — это параметр "name" в path()
    template_name = "registration/register.html"


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'


class UserProfileView(DetailView):
    template_name = 'profile.html'
    model = NewUser
    context_object_name = 'user'

    def get_context_data(self, *args, **kwargs):
        users = NewUser.objects.all()
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(NewUser, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

