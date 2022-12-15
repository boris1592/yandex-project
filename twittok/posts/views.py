from django.views import View
from django.views.generic import ListView

from twittok.settings import POSTS_PER_PAGE

from .models import Post


class RecommendedPostsView(ListView):
    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.recommended(self.request.user.id, POSTS_PER_PAGE)


class RateView(View):
    def post(self, request, pk, rating):
        pass
