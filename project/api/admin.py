from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Article, History, Place, Tag, Question, Event, City


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')
    search_fields = ('title', 'color')
    list_filter = ('title',)
    empty_value_display = _('-пусто-')


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'imageUrl')
    search_fields = ('title', 'imageUrl')
    list_filter = ('title',)
    empty_value_display = _('-пусто-')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    list_filter = ('title',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'info', 'description', 'imageUrl', 'link')
    search_fields = ('title', 'name', 'info')
    list_filter = ('name',)
    empty_value_display = _('-пусто-')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = _('-пусто-')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name',)
    empty_value_display = _('-пусто-')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact', 'title',
                    'description', 'start_at', 'end_at', 'seats', 'city')
    search_fields = ('name', 'city')
    list_filter = ('name',)
    empty_value_display = _('-пусто-')
