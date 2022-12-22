from json import dumps

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import FormView
from posts.models import Tag

from .forms import SignupForm


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'auth/sign_up.html'
    success_url = '/users/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = dumps(
            list(map(lambda t: t.name, Tag.objects.filter(is_default=True)))
        )
        return context

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
        )
        login(self.request, user)
        return super().form_valid(form)
