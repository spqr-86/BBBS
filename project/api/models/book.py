from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..validators import year_validator


class Book(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    author = models.CharField(
        verbose_name=_('Автор'),
        max_length=256,
    )
    year = models.SmallIntegerField(
        verbose_name=_('Год публикации'),
        validators=[year_validator],
    )
    annotation = models.TextField(
        verbose_name=_('Аннотация'),
        max_length=1024,
    )
    type = models.ForeignKey(
        'api.BookType',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Тип'),
        related_name='books'
    )
    url = models.URLField(
        verbose_name=_('Ссылка')
    )

    def colortile(self):
        if self.color:
            return format_html('<div style="background-color: {0}; \
                height: 100px; width: 100px"></div>', self.color)
        return 'пусто'

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')
        indexes = [
            models.Index(fields=['type'], name='book_type_slug_index')
        ]

    def __str__(self):
        return self.title
