from django.shortcuts import render
from django.views import View

from twittok.settings import POSTS_PER_PAGE

from . import models


class PostsView(View):
    def get(self, request):
        posts = models.Post.objects.raw(
            '''
            select *, (
                select count(posts_postrating.id)
                from posts_postrating
                where posts_postrating.post_id = posts_post.id
                and posts_postrating.user_id = %s
            ) as ratings_count, (
                select sum((
                    select avg(posts_postrating.rating)
                    from posts_postrating
                    join posts_post_tags
                        on posts_post_tags.post_id = posts_postrating.post_id
                    where posts_post_tags.tag_id = posts_tag.id
                    and posts_postrating.user_id = %s
                )) as rating
                from posts_tag
                join posts_post_tags on posts_tag.id = posts_post_tags.tag_id
                where posts_post_tags.post_id = posts_post.id
            ) as factor
            from posts_post
            where ratings_count = 0
            order by factor desc
            limit %s
            ''',
            [request.user.id, request.user.id, POSTS_PER_PAGE],
        )
        return render(request, 'posts.html', {'posts': posts})
