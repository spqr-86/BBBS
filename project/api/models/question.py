from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    tags = models.ManyToManyField(
        'api.Tag',
<<<<<<< HEAD
        verbose_name=_('Теги'),
=======
        verbose_name=_('Тег(и)'),
>>>>>>> main
        related_name='questions',
    )

    class Meta:
        app_label = 'api'
<<<<<<< HEAD
        ordering = ['id']
=======
        ordering = ('id',)
>>>>>>> main
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.title
