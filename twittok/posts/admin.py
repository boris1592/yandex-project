from django.contrib import admin

from .models import Post, PostRating, PreferredTag, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    filter_horizontal = ('tags',)


@admin.register(PreferredTag)
class PreferredTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_display_links = ('tag',)


@admin.register(PostRating)
class PostRatingAdmin(admin.ModelAdmin):
    list_display = ('post',)
    list_display_links = ('post',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
