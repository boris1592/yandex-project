from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    filter_horizontal = ('tags',)


@admin.register(models.PostRating)
class PostRatingAdmin(admin.ModelAdmin):
    list_display = ('post',)
    list_display_links = ('post',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
