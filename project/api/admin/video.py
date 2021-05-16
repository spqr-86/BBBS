from django.contrib import admin

from ..models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_url', 'link')
    search_fields = ('title',)
    empty_value_display = '-пусто-'
