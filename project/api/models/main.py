<<<<<<< HEAD
from django.core.exceptions import ValidationError
=======
>>>>>>> main
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _


class Main(models.Model):
    title = CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    events = ManyToManyField(
        'api.Event',
        verbose_name=_('События'),
    )
    histories = ManyToManyField(
        'api.History',
        verbose_name=_('Истории'),
    )
    places = ManyToManyField(
        'api.Place',
        verbose_name=_('Места'),
    )
    articles = ManyToManyField(
        'api.Article',
        verbose_name=_('Статьи'),
    )
    movies = ManyToManyField(
        'api.Movie',
        verbose_name=_('Фильмы'),
    )
    video = ManyToManyField(
        'api.Video',
        verbose_name=_('Видео'),
    )
    questions = ManyToManyField(
        'api.Question',
        verbose_name=_('Вопросы'),
    )

    class Meta:
        app_label = 'api'
<<<<<<< HEAD
        ordering = ['id']
=======
        ordering = ('id',)
>>>>>>> main
        verbose_name = _('Главная страница')
        verbose_name_plural = _('Главная страница')
