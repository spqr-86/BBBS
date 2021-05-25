from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_('Пользователь'),
        null=False,
    )
    city = models.ForeignKey(
        'api.City',
        on_delete=models.CASCADE,
        related_name='profiles',
        verbose_name=_('Город'),
        null=False,
    )

    class Meta:
        app_label = 'api'
        ordering = ['-id']
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self):
        return f'{self.user}, {self.city}'
