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
    duration = models.PositiveIntegerField(
        verbose_name=_('Продолжительность видеоролика в сек.'),
        default=0,
        validators=(MinValueValidator(1), MaxValueValidator(86400)),
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Теги'),
        related_name='videos',
        blank=True,
    )
    output_to_main = models.BooleanField(
        verbose_name=_('Отображать на главной странице'),
        default=False,
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Видеоролик')
        verbose_name_plural = _('Видеоролики')

    def __str__(self):
        return self.title
