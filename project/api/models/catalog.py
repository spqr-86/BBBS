from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from .mixins import ImageFromUrlMixin


class Catalog(models.Model, ImageFromUrlMixin):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
    )
    image = models.ImageField(
        upload_to='catalogs/',
        verbose_name=_('Фото'),
        blank=True,
        null=True
    )
    content = HTMLField()

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Справочник')
        verbose_name_plural = _('Справочник')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        if self.image_url and not self.image:
            self.load_image(image_url=self.image_url)
        return super().save(*args, **kwargs)
