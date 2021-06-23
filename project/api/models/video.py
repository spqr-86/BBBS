import requests
import urllib
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_image_url_from_link(video_url: str) -> str:
    '''для получения url независимо от вида ссылки на видео youtube'''
    try:
        response = requests.get(video_url)
        desired_url = response.url
        parsed_url = urllib.parse.urlparse(desired_url)
        parameters = urllib.parse.parse_qs(parsed_url.query)
        video_id = parameters['v'][0]
        video_thumbnail_url = f'https://img.youtube.com/vi/{video_id}/0.jpg'
        return video_thumbnail_url
    except requests.exceptions.ConnectionError:
        raise ConnectionError


class Video(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    info = models.TextField(
        verbose_name=_('Информация'),
        max_length=512,
    )
    image = models.ImageField(
        upload_to='videos/',
        blank=True,
        null=True
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

    def save(self, *args, **kwargs) -> None:
        if Video.objects.exists():
            new_id = Video.objects.latest('id').id + 1
        else:
            new_id = 1
        if self.link and not self.image:
            try:
                video_thumbnail_url = get_image_url_from_link(self.link)
                response = requests.get(video_thumbnail_url)
                image = open(
                    settings.MEDIA_ROOT / f'{Video.image.field.upload_to}{new_id}_pic.jpg', 'wb'
                )
                image.write(response.content)
                image.close()
                self.image = image.name
            except ConnectionError:
                return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
