from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_('Пользователь'),
    )
    city = models.ForeignKey(
        'api.City',
        verbose_name=_('Город'),
        related_name='profiles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    region = models.ForeignKey(
        'api.Region',
        verbose_name=_('Регион'),
        related_name='profiles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = Profile.objects.get_or_create(user=instance)
