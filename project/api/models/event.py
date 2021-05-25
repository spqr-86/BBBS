from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from . import City

User = get_user_model()


class Event(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False,
        auto_created=True,
    )
    participant = models.ManyToManyField(
        User,
        verbose_name='Записавшиеся юзеры',
        default=None,
        blank=True,
    )
    address = models.CharField(
        verbose_name='Адрес мероприятия',
        max_length=200,
    )
    contact = models.CharField(
        verbose_name='Контактное лицо',
        max_length=200,
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Описание мероприятия',
    )
    start_at = models.DateTimeField(
        verbose_name='Время начала',
    )
    end_at = models.DateTimeField(
        verbose_name='Время окончания',
    )
    seats = models.IntegerField(
        verbose_name='Максимальное число участников',
    )
    taken_seats = models.IntegerField(
        verbose_name='Число записавшихся',
        default=0,
    )
    city = models.ForeignKey(
        City,
        verbose_name='Город мероприятия',
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Event)
def get_taken_seats(sender, instance, **kwargs):
    if instance.participant:
        instance.taken_seats = instance.participant.count()
