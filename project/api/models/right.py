from django.db import models
from django.utils.translation import gettext_lazy as _


class Right(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    description = models.CharField(
        verbose_name=_('Описание'),
        max_length=500,
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Тег(и)'),
        related_name='rights',
        limit_choices_to={'category': _('Права')},
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Право')
        verbose_name_plural = _('Права')

    def __str__(self):
        return self.title


class RightContent(models.Model):
    right = models.ForeignKey(
        Right,
        verbose_name=_('Статья'),
        related_name='content',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    block_type = models.CharField(
        verbose_name=_('Тип контента'),
        max_length=4,
        choices=(('text', _('Абзац')), ('list', _('Список'))),
    )
    text_blocks = models.ManyToManyField(
        'common.TextBlock',
        verbose_name=_('Блоки текста'),
        related_name='rights',
    )
    colored_back = models.BooleanField(
        verbose_name=_('Раскрашенный фон'),
        default=False,
    )
    order = models.PositiveSmallIntegerField(
        verbose_name=_('Порядок вывода'),
        default=0,
    )

    class Meta:
        app_label = 'api'
        ordering = ('order',)
        verbose_name = _('Содержание статьи')
        verbose_name_plural = _('Содержание статьи')

    def __str__(self):
        return self.title
