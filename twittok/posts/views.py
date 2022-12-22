from json import loads

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import FormView, ListView

from twittok.settings import POSTS_PER_PAGE

from .forms import CreatePostForm
from .models import Post, PostRating, Tag


class RecommendedPostsView(ListView):
    template_name = 'posts/recommended_posts.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.recommended(self.request.user.id, POSTS_PER_PAGE)


class RateView(View):
    def get(self, request, pk, rating):
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
    template_name = 'posts_new_posts.html'
    success_url = '/users/profile/'

    def form_valid(self, form):
        tags_in_form = loads(form.cleaned_data['tags'])
        tags = []

        for tag_name in map(lambda t: t['value'].lower(), tags_in_form):
            tags_with_name = Tag.objects.filter(name=tag_name)
            tags.append(
                tags_with_name.first()
                if tags_with_name.exists()
                else Tag.objects.create(name=tag_name)
            )

        post = Post.objects.create(
            title=form.cleaned_data['title'],
            text=form.cleaned_data['text'],
            user=self.request.user,
        )
        post.tags.set(tags)
        return super().form_valid(form)


class MyPostsView(ListView):
    template_name = 'posts/my_posts.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user__id=self.request.user.id)
