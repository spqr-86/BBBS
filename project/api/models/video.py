from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Video(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    info = models.TextField(
        verbose_name=_('Информация'),
        max_length=512,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
    )
    link = models.URLField(
        verbose_name=_('Ссылка на видеоролик'),
        max_length=192,
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name=_('Продолжительность видеоролика'),
        default=0,
        validators=(MinValueValidator(1), MaxValueValidator(1440))
    )

    class Meta:
        app_label = 'api'
        verbose_name = _('Видеоролик')
        verbose_name_plural = _('Видеоролики')

    def __str__(self):
        return self.title
