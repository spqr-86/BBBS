from django_filters import CharFilter, FilterSet, NumberFilter

from .models import Place


class PlaceFilter(FilterSet):
    min_age = NumberFilter(field_name='age', lookup_expr='gte')
    max_age = NumberFilter(field_name='age', lookup_expr='lte')
    tags = CharFilter(field_name='tags__slug')

    class Meta:
        model = Place
        fields = ['age', 'tags']
