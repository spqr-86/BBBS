from django.contrib import admin

from .models import Place, Tag


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'info', 'description', 'imageUrl', 'link')
    search_fields = ('title', 'name', 'info')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = '-пусто-'
