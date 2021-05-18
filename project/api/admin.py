from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .fields import fields
from .models import Article, History, Movie, Place, Question, Tag, Video


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')
    search_fields = ('title', 'color')
    empty_value_display = _('-пусто-')
    formfield_overrides = {
        fields.ColorField: {'widget': forms.TextInput(attrs={'type': 'color',
                            'style': 'height: 100px; width: 100px;'})}
    }


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url')
    search_fields = ('title', 'image_url')
    empty_value_display = _('-пусто-')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_url', 'link')
    search_fields = ('title',)
    list_filter = ('tags', )
    empty_value_display = _('-пусто-')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    list_filter = ('tags', )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'info', 'image_url', 'link')
    search_fields = ('title', 'name', 'info')
    empty_value_display = _('-пусто-')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_url', 'link', 'duration')
    search_fields = ('title',)
    empty_value_display = _('-пусто-')
