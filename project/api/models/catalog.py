from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..validators import file_size_validator, image_extension_validator
from .mixins import ImageFromUrlMixin


class Catalog(models.Model, ImageFromUrlMixin):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    image = models.ImageField(
        upload_to='catalogs/',
        verbose_name=_('Изображение'),
        blank=True,
        null=True,
        help_text=_(
            f'Поддерживаемые форматы {", ".join(settings.IMAGE_EXTENSIONS)}. \
             Размер до 10М.'
        ),
        validators=[file_size_validator, image_extension_validator],
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
        help_text=_('Альтернативный способ загрузки изображения. \
                     Приоритет у файла.'),
    )
    raw_html = models.TextField(
        verbose_name=_('HTML'),
        max_length=4 * 10 ** 6,
        help_text=_('Поле для html кода страницы.'),
    )

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
        self.raw_html = ' '.join(self.raw_html.split())
        return super().save(*args, **kwargs)
