from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from .forms import CreationForm, LoginUserForm, AddressForm, UserProfileForm
from .models import User, Address, Order


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'


def is_own_profile(user, pk):
    return user.is_authenticated and user.pk == pk


class UserProfileView(DetailView):
    template_name = 'profile.html'
    model = User
    context_object_name = 'user'

    def dispatch(self, request, *args, **kwargs):
        # Проверка доступа перед выполнением view
        if not is_own_profile(request.user, kwargs['pk']):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['addresses'] = user.addresses.all()

        # Получение заказов пользователя и добавление их в контекст
        orders = Order.objects.filter(user=user).order_by('-order_date')
        context['orders'] = orders

        return context

    def handle_no_permission(self):
        # Обработка ошибки отсутствия доступа
        raise PermissionDenied("У вас нет доступа к этому профилю.")


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


def delete_address(request, pk):
    address = get_object_or_404(Address, id=pk)
    # Проверяем, чтобы пользователь мог удалять только свои адреса
    if address.user == request.user:
        address.delete()

    return redirect('profile', pk=request.user.pk)


def logout_view(request):
    logout(request)
    return redirect('index')
