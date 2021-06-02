from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _

from . import models
from .fields import fields

User = get_user_model()


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
    list_display = ('id', 'name', 'region', 'is_primary')
    search_fields = ('name', )
    list_filter = ('region', 'is_primary')
    autocomplete_fields = ('region', )


@admin.register(models.Event)
class EventAdmin(MixinAdmin):
    list_display = ('id', 'title', 'start_at', 'end_at', 'city', 'taken_seats')
    search_fields = ('title', 'contact', 'address', 'city')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.has_perm('api.events_in_all_cities'):
            return queryset
        return queryset.filter(city__in=request.user.region.cities.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user
        if (db_field.name == 'city'
                and not user.has_perm('api.events_in_all_cities')):
            kwargs['queryset'] = models.City.objects.filter(region=user.region)
        return super(
            EventAdmin,
            self
        ).formfield_for_foreignkey(db_field, request, **kwargs)

    def taken_seats(self, obj):
        from django.utils.html import format_html
        count = obj.participants.count()
        url = (
            reverse('admin:account_customuser_changelist')
            + '?'
            + urlencode({'events__id': f'{obj.id}'})
        )
        return format_html('<a href="{}">{} чел.</a>', url, count)

    taken_seats.short_description = 'Кол-во участников'


@admin.register(models.History)
class HistoryAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url')
    search_fields = ('title', 'image_url')


@admin.register(models.Main)
class MainAdmin(MixinAdmin):
    list_display = ('id', 'title')
    filter_horizontal = ('articles', 'movies', 'questions')
    autocomplete_fields = ('history', 'video')


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
    list_display = ('id', 'title', 'name', 'info', 'image_url', 'link', 'city')
    search_fields = ('title', 'name', 'info')
    list_filter = ('city', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.has_perm('api.places_in_all_cities'):
            return queryset
        return queryset.filter(city__in=request.user.region.cities.all())

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user
        if (db_field.name == 'city'
                and not user.has_perm('api.places_in_all_cities')):
            kwargs['queryset'] = models.City.objects.filter(region=user.region)
        return super(
            PlaceAdmin,
            self
        ).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.Region)
class RegionAdmin(MixinAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(models.Tag)
class TagAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Video)
class VideoAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url', 'link', 'duration')
    search_fields = ('title',)
