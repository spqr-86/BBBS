from django.contrib.auth import get_user_model
from django.db import models

from BBBS.project.api.models.cityes import City


User = get_user_model()


class Event(models.Model):
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


class EventParticipant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, on_delete=models.RESTRICT)