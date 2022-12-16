from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class PostManager(models.Manager):
    def recommended(self, user_id, limit):
        return Post.objects.raw(
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
            [user_id, user_id, limit],
        )


class Post(models.Model):
    objects = PostManager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    tags = models.ManyToManyField(Tag)


class PostRating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(
        default=0, validators=[MinValueValidator(-1), MaxValueValidator(1)]
    )

    class Meta:
        unique_together = ('user', 'post')
