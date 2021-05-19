from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models
from .fields import fields


class MixinAdmin(admin.ModelAdmin):
    empty_value_display = _('-пусто-')


@admin.register(models.Article)
class ArticleAdmin(MixinAdmin):
    list_display = ('id', 'title', 'color')
    search_fields = ('title', 'color')
    formfield_overrides = {
        fields.ColorField: {'widget': forms.TextInput(attrs={'type': 'color',
                            'style': 'height: 100px; width: 100px;'})}
    }


@admin.register(models.City)
class CityAdmin(MixinAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(models.Event)
class EventAdmin(MixinAdmin):
    list_display = ('id', 'title', 'start_at', 'end_at', 'city')
    search_fields = ('title', 'contact', 'address', 'city')


@admin.register(models.History)
class HistoryAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url')
    search_fields = ('title', 'image_url')


@admin.register(models.Movie)
class MovieAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url', 'link')
    search_fields = ('title',)
    list_filter = ('tags', )
    autocomplete_fields = ('tags', )


@admin.register(models.Question)
class QuestionAdmin(MixinAdmin):
    list_display = ('id', 'title', )
    search_fields = ('title', )
    list_filter = ('tags', )
    autocomplete_fields = ('tags', )


@admin.register(models.Place)
class PlaceAdmin(MixinAdmin):
    list_display = ('id', 'title', 'name', 'info', 'image_url', 'link')
    search_fields = ('title', 'name', 'info')


@admin.register(models.Tag)
class TagAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Video)
class VideoAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url', 'link', 'duration')
    search_fields = ('title',)
