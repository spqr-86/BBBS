from django.db import models


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True,
    )

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.slug
