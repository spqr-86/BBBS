from django.db import models
from django.utils.translation import gettext as _

#from . import Tag


class Question(models.Model):
    title = models.CharField(
        verbose_name=_('Заглавие'),
        max_length=200,
    )
#    tags = models.ForeignKey(
#        Tag,
#        verbose_name=_('Тэг'),
#        related_name='question',
#        on_delete=models.CASCADE
#    )

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.title
