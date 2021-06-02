from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils.translation import gettext_lazy as _


class Main(models.Model):
    title = CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    history = ForeignKey(
        'api.History',
        verbose_name=_('Истории'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    articles = ManyToManyField(
        'api.Article',
        verbose_name=_('Статьи'),
    )
    movies = ManyToManyField(
        'api.Movie',
        verbose_name=_('Фильмы'),
    )
    video = ForeignKey(
        'api.Video',
        verbose_name=_('Видео'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    questions = ManyToManyField(
        'api.Question',
        verbose_name=_('Вопросы'),
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Главная страница')
        verbose_name_plural = _('Главная страница')
