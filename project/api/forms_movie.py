from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags and tags.count() > settings.MAX_TAGS_COUNT:
            raise ValidationError(f'Можно выбрать максимум 4 тега')
        return tags
