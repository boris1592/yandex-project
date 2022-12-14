from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib.auth.models import User

from .forms import SignupForm


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'form_page.html'
    success_url = '/users/profile'

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
        )
        login(self.request, user)
        return super().form_valid(form)
