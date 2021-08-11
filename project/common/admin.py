from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class MixinAdmin(admin.ModelAdmin):
    empty_value_display = _('-пусто-')


@admin.register(models.TextBlock)
class TextBlockAdmin(MixinAdmin):
    list_display = ('id', 'text')
    search_fields = ('text', )
