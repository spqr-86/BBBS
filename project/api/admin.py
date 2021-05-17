from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Place, Tag


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'info', 'imageUrl', 'link')
    search_fields = ('title', 'name', 'info')
    list_filter = ('name',)
    empty_value_display = _('-пусто-')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = _('-пусто-')
