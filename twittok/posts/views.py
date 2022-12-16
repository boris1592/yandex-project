from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from twittok.settings import POSTS_PER_PAGE

from .models import Post, PostRating


class RecommendedPostsView(ListView):
    template_name = 'posts.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.recommended(self.request.user.id, POSTS_PER_PAGE)


class RateView(View):
    def post(self, request, pk, rating):
        get_object_or_404(Post, pk=pk)
        post_rating = PostRating.objects.filter(
            post_id=pk,
            user_id=request.user.id
        ).first()

        if post_rating is None:
            post_rating = PostRating(post_id=pk, user_id=request.user.id)

        post_rating.rating = rating
        post_rating.save()
        return HttpResponse(status=201)
