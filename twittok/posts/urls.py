from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import RecommendedPostsView

app_name = 'posts'

urlpatterns = [
    path(
        'recommended/',
        login_required(RecommendedPostsView.as_view()),
        name='recommended',
    )
]
