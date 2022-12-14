from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)


class TagStats(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
