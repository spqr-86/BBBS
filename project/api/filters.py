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
    months = CharFilter(field_name='start_at', method='filter_months')
    years = CharFilter(field_name='start_at', method='filter_years')

    def filter_months(self, queryset, slug, months):
        return queryset.filter(start_at__month__in=months.split(','))

    def filter_years(self, queryset, slug, years):
        return queryset.filter(start_at__year__in=years.split(','))

    class Meta:
        model = Event
        fields = ['months', 'years']
