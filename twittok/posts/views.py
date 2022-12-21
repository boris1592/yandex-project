from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import FormView, ListView

from twittok.settings import POSTS_PER_PAGE

from .forms import CreatePostForm
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
            post_id=pk, user_id=request.user.id
        ).first()

        if post_rating is None:
            post_rating = PostRating(post_id=pk, user_id=request.user.id)

        post_rating.rating = rating
        post_rating.save()
        return HttpResponse(status=201)


class CreateRateView(FormView):
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = '/users/profile/'

    def form_valid(self, form):
        Post.objects.create(
            title=form.cleaned_data['title'],
            text=form.cleaned_data['text'],
            user=self.request.user,
        )
        return super().form_valid(form)
