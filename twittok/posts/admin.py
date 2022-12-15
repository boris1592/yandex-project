from django.contrib import admin

from .models import Post, PostRating, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    filter_horizontal = ('tags',)


@admin.register(PostRating)
class PostRatingAdmin(admin.ModelAdmin):
    list_display = ('post',)
    list_display_links = ('post',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
