from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=200,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    info = models.CharField(
        verbose_name='Info',
    )
    description = models.TextField(
        verbose_name='Description',
    )
    imageUrl = models.URLField(
        verbose_name='Image',
    )
    link = models.URLField(
        verbose_name='Link',
    )

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.title
