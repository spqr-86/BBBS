from django.db import models
from django.utils.translation import gettext_lazy as _


class Place(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=200,
    )
    info = models.CharField(
        verbose_name=_('Информация'),
        max_length=500,
    )
    description = models.TextField(
        verbose_name=_('Описание'),
    )
    image_url = models.URLField(
        verbose_name=_('Изображение'),
        blank=True,
        null=True,
    )
    link = models.URLField(
        verbose_name=_('Ссылка'),
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        'api.City',
        verbose_name=_('Город'),
        related_name='places',
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Место')
        verbose_name_plural = _('Места')
        permissions = (
            ('places_in_all_cities', _('Можно смотреть места всех городов')),
        )

    def __str__(self):
        return self.title
