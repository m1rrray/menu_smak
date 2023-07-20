"""
URL configuration for smak_menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import SignUp, LoginUser, UserProfileView, logout_view, add_address, edit_profile, \
    addresses, delete_address

urlpatterns = [
    # path("auth/", include("users.urls")),
    # path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', SignUp.as_view(), name='register'),
    path('cart/', include('cart.urls')),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/add_address/', add_address, name='add_address'),
    path('profile/<int:pk>/edit_profile/', edit_profile, name='edit_profile'),
    path('profile/<int:pk>/edit_addresses/', addresses, name='edit_address'),
    path('profile/delete_address/<int:pk>/', delete_address, name='delete_address'),
    path('logout/', logout_view, name='logout'),
    path("", include("posts.urls")),


]
