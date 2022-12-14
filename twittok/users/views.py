from django.views.generic import FormView
from .forms import SignupForm
from django.contrib.auth.models import User


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'form_page.html'
    success_url = '/users/login'

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
        )
        return super().form_valid(form)
