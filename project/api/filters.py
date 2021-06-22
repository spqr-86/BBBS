from django_filters import CharFilter, FilterSet, NumberFilter

from .models import Event, Place


class PlaceFilter(FilterSet):
    min_age = NumberFilter(field_name='age', lookup_expr='gte')
    max_age = NumberFilter(field_name='age', lookup_expr='lte')
    tags = CharFilter(field_name='tags__slug')

    class Meta:
        model = Place
        fields = ['age', 'tags']


class EventFilter(FilterSet):
    month = NumberFilter(field_name='start_at', lookup_expr='month')
    year = NumberFilter(field_name='start_at', lookup_expr='year')

    class Meta:
        model = Event
        fields = ['month', 'year']
