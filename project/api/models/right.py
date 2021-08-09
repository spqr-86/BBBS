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
    text_blocks = models.ManyToManyField(
        'api.TextBlock',
        verbose_name=_('Абзацы'),
        related_name='rights',
    )
    list_block = models.TextField(
        verbose_name=_('Список тезисов'),
        blank=True,
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
