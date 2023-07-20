from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import CreationForm, LoginUserForm, AddressForm, UserProfileForm
from .models import User, Address


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')  # где login — это параметр "name" в path()
    template_name = "registration/register.html"


class LoginUser(LoginView):
    form_class = LoginUserForm
    print(form_class)
    template_name = 'registration/login.html'


class UserProfileView(DetailView):
    template_name = 'profile.html'
    model = User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()  # получаем текущего пользователя
        context['addresses'] = user.addresses.all()  # получаем все адреса текущего пользователя

        return context


def add_address(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = Address(**form.cleaned_data)
            address.user = user
            address.save()
            user.addresses.add(address)
            user.save()
            return redirect('profile', pk=pk)
    else:
        form = AddressForm()
    form = AddressForm()

    return render(request, 'add_address.html', {'form': form})


@login_required
def edit_profile(request, pk):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=pk)
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})



@login_required
def addresses(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'addresses': user.addresses.all(),
        'user': user,
    }
    return render(request, 'address_edit.html', context)


def delete_address(request):
    # Получаем объект адреса или 404, если адрес не существует
    # address = Address.objects.get()
    # address.delete()
    return redirect('index.html')
    # return render(request, 'index.html', {})

def delete_address(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)


def logout_view(request):
    logout(request)
    return redirect('index')

