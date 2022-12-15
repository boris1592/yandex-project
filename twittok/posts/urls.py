from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path(
        'recommended/',
        login_required(views.PostsView.as_view()),
        name='recommended',
    )
]
