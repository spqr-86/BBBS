from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models
from .fields import ColorField


class MixinAdmin(admin.ModelAdmin):
    empty_value_display = _('-пусто-')


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ('date_joined', 'last_login')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()
        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }
        if (
            not is_superuser
            and obj is not None
            and (obj.is_superuser or obj == request.user)
        ):
            disabled_fields |= {
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form


@admin.register(models.Article)
class ArticleAdmin(MixinAdmin):
    list_display = ('id', 'title', 'color')
    search_fields = ('title', 'color')
    formfield_overrides = {
        ColorField: {'widget': forms.TextInput(attrs={
            'type': 'color',
            'style': 'height: 100px;width: 100px;'})}
    }


@admin.register(models.City)
class CityAdmin(MixinAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(models.Event)
class EventAdmin(MixinAdmin):
    list_display = ('id', 'title', 'start_at', 'end_at', 'city')
    search_fields = ('title', 'contact', 'address', 'city')
    autocomplete_fields = ('city', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.has_perm('api.view_all_cities'):
            return queryset
        return queryset.filter(city__in=request.user.profile.cities.all())


@admin.register(models.History)
class HistoryAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url')
    search_fields = ('title', 'image_url')


@admin.register(models.Main)
class MainAdmin(MixinAdmin):
    list_display = ('id', 'title')
    filter_horizontal = ('events', 'histories', 'places', 'articles',
                         'movies', 'video', 'questions')


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


@admin.register(models.Participant)
class ParticipantAdmin(MixinAdmin):
    list_display = ('id', 'event', 'participant')
    search_fields = ('event', 'participant')
    autocomplete_fields = ('event', 'participant')


@admin.register(models.Profile)
class ProfileAdmin(MixinAdmin):
    list_display = ('id', 'user')
    search_fields = ('user', 'city')
    list_filter = ('cities', )
    autocomplete_fields = ('cities', )


@admin.register(models.Tag)
class TagAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Video)
class VideoAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url', 'link', 'duration')
    search_fields = ('title',)
