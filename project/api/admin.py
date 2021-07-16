from django.forms import TextInput
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _

from . import forms, models
from .fields import fields


User = get_user_model()


class MixinAdmin(admin.ModelAdmin):
    empty_value_display = _('-пусто-')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tags':
            kwargs['queryset'] = models.Tag.objects.filter(
                category=self.model._meta.verbose_name_plural
            )
        return super(
            MixinAdmin,
            self
        ).formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(models.ActivityType)
class ActivityAdmin(MixinAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )


@admin.register(models.Article)
class ArticleAdmin(MixinAdmin):
    list_display = ('id', 'title', 'pinned_full_size')
    search_fields = ('title', )
    list_filter = ('pinned_full_size', )


@admin.register(models.BookType)
class BookTypeAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug', 'color')
    search_fields = ('name', 'slug', 'color')
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        fields.ColorField: {'widget': TextInput(attrs={'type': 'color',
                            'style': 'height: 100px; width: 100px;'})}
    }


@admin.register(models.Book)
class BookAdmin(MixinAdmin):
    list_display = ('id', 'title', 'author', 'year', 'type', 'get_color')
    list_filter = ('type', )
    search_fields = ('title', 'info', 'color')

    @admin.display(description=_('Цвет'))
    def get_color(self, obj):
        try:
            color = obj.type.color
        except AttributeError:
            color = None
        return color
    get_color.admin_order_field = 'color'


@admin.register(models.Catalog)
class CatalogAdmin(MixinAdmin):
    list_display = ('id', 'title', 'image_url')
    search_fields = ('title', )


@admin.register(models.City)
class CityAdmin(MixinAdmin):
    list_display = ('id', 'name', 'region', 'is_primary')
    search_fields = ('name', )
    list_filter = ('region', 'is_primary')
    autocomplete_fields = ('region', )


@admin.register(models.Diary)
class DiaryAdmin(MixinAdmin):
    list_display = ('id', 'mentor', 'place', 'date', 'mark')
    search_fields = ('place', )


@admin.register(models.Event)
class EventAdmin(MixinAdmin):
    list_display = ('id', 'title', 'get_start_at',
                    'get_end_at', 'city', 'taken_seats', 'seats')
    list_filter = ('tags', )
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
        if db_field.name == 'tags':
            kwargs['queryset'] = models.Tag.objects.filter(
                category=self.model._meta.verbose_name_plural
            )
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

    @admin.display(description=_('Время начала'))
    def get_start_at(self, obj):
        return obj.start_at.strftime('%Y-%m-%d %H:%M')

    @admin.display(description=_('Время окончания'))
    def get_end_at(self, obj):
        return obj.end_at.strftime('%Y-%m-%d %H:%M')


@admin.register(models.History)
class HistoryAdmin(MixinAdmin):
    list_display = ('id', 'title', 'mentor', 'child')
    search_fields = ('title', )
    list_filter = ('mentor', 'child')


@admin.register(models.Movie)
class MovieAdmin(MixinAdmin):
    form = forms.MovieForm
    list_display = ('id', 'title', 'link', 'image_tag')
    search_fields = ('title',)
    list_filter = ('tags', )
    readonly_fields = ('image_tag',)

    def image_tag(self, instance):
        return format_html(
            '<img src="{0}" style="max-height: 50px"/>',
            instance.image.url
        )


@admin.register(models.Question)
class QuestionAdmin(MixinAdmin):
    list_display = ('id', 'title', 'get_answer')
    search_fields = ('title', )
    list_filter = ('tags', )

    @admin.display(description=_('Ответ'))
    def get_answer(self, obj):
        answer = obj.answer
        if answer is not None:
            return f'{answer[:50]}..'
        return answer


@admin.register(models.Place)
class PlaceAdmin(MixinAdmin):
    list_display = ('id', 'title', 'address', 'link', 'city', 'activity_type',
                    'age', 'age_restriction', 'moderation_flag')
    list_editable = ('age_restriction', )
    search_fields = ('title', 'name', 'info')
    list_filter = ('city', 'activity_type',
                   'age_restriction', 'moderation_flag', 'tags')
    radio_fields = {'gender': admin.HORIZONTAL}
    readonly_fields = ('image_tag',)

    def image_tag(self, instance):
        return format_html(
            '<img src="{0}" style="max-height: 50px"/>',
            instance.image.url
        )

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


@admin.register(models.Right)
class RightAdmin(MixinAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('tags', )


@admin.register(models.Region)
class RegionAdmin(MixinAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(models.Tag)
class TagAdmin(MixinAdmin):
    list_display = ('id', 'name', 'category', 'slug')
    list_editable = ('category', )
    search_fields = ('name', 'category', 'slug')
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Video)
class VideoAdmin(MixinAdmin):
    list_display = ('id', 'title', 'link', 'image_tag',
                    'duration', 'pinned_full_size')
    search_fields = ('title', )
    list_filter = ('pinned_full_size', 'resource_group')
    readonly_fields = ('image_tag',)

    def image_tag(self, instance):
        return format_html(
            '<img src="{0}" style="max-height: 50px"/>',
            instance.image.url
        )
