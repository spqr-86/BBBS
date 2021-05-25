from django.db import models


class City(models.Model):
    id = models.IntegerField(
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='Город',
        max_length=128,

    )
    isPrimary = models.BooleanField(
        verbose_name='Город пользователя',
    )

    def __str__(self):
        return self.id
