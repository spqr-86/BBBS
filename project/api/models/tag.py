from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=50,
    )
    category = models.CharField(
        verbose_name=_('Категория'),
        max_length=50,
        choices=(
            (_('Книги'), _('Книги')),
            (_('Фильмы'), _('Фильмы')),
            (_('Места'), _('Места')),
            (_('Вопросы'), _('Вопросы')),
            (_('Права'), _('Права')),
            (_('Видеоролики'), _('Видеоролики')),
            (_('События'), _('События')),
        ),
    )
    slug = models.SlugField(
        verbose_name=_('Слаг (Ссылка)'),
        unique=True,
    )

    class Meta:
        app_label = 'api'
        ordering = ('category', 'name')
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __str__(self):
        return f'{self.category}: {self.name}'
