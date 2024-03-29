from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls.converters import register_converter

from .converters import PkConverter, RatingConverter
from .views import CreateRateView, MyPostsView, RateView, RecommendedPostsView

register_converter(PkConverter, 'pk')
register_converter(RatingConverter, 'rating')

app_name = 'posts'

urlpatterns = [
    path(
        'recommended/',
        login_required(RecommendedPostsView.as_view()),
        name='recommended',
    ),
    path(
        'rate/<pk:pk>/<rating:rating>',
        login_required(RateView.as_view()),
        name='rate',
    ),
    path(
        'create/',
        login_required(CreateRateView.as_view()),
        name='create',
    ),
    path(
        'my_posts/',
        login_required(MyPostsView.as_view()),
        name='my',
    ),
]
