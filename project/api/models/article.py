from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import ImageFromUrlMixin


class Article(models.Model, ImageFromUrlMixin):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    info = models.CharField(
        verbose_name=_('Информация'),
        max_length=200,
    )
    annotation = models.TextField(
        verbose_name=_('Аннотация'),
        max_length=1024,
    )
    article_url = models.URLField(
        verbose_name=_('Ссылка на статью'),
        max_length=192,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='articles/',
        verbose_name=_('Фото'),
        blank=True,
        null=True,
    )
    output_to_main = models.BooleanField(
        verbose_name=_('Отображать на главной странице'),
        default=False,
    )
    pinned_full_size = models.BooleanField(
        verbose_name=_('Отображать с полноразмерным '
                       'изображением вверху страницы'),
        default=False,
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        if Article.objects.exists():
            print('exists')
        else:
            print('doesn\'t exist')
        if self.image_url and not self.image:
            self.load_image(image_url=self.image_url)
        if self.pinned_full_size:
            self.__class__.objects.filter(pinned_full_size=True).update(pinned_full_size=False)  # noqa E501
        return super().save(*args, **kwargs)
