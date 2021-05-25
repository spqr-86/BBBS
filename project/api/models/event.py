from django.contrib.auth import get_user_model
from django.db import models

from . import City

User = get_user_model()


class Event(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
    )
    booked = models.BooleanField(
        default=False,
    )
    participant = models.OneToOneField(
        User,
        on_delete=models.RESTRICT,
        verbose_name='Записавшиеся юзеры',
        default=None,
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
