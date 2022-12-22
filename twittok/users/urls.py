from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from .forms import LoginForm
from .views import SignupView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(
            template_name='auth/sign_in.html', authentication_form=LoginForm
        ),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='logout.html'),
        name='logout',
    ),
    path(
        'profile/',
        login_required(TemplateView.as_view(template_name='profile.html')),
        name='profile',
    ),
]
