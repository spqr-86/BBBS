from django.contrib.postgres.search import (SearchVector, SearchQuery,
                                            SearchRank)
from django.urls import reverse
from django.utils.timezone import now
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ..models import Article, Event, Place, Book, Movie, Video, Right, Question
from ..serializers import SearchResultSerializer

SELECT_VALUE = '\'{model._meta.verbose_name_plural}\''
NAMESPACE = 'api:v1:'
REVERSE_VIEWNAME_TEMPLATE = '%s{model}-list' % NAMESPACE


def get_path(model):
    return reverse(
        REVERSE_VIEWNAME_TEMPLATE.format(model=model.__name__.lower())
    )


def build_select_dict(model):
    return {
        'model_name': SELECT_VALUE.format(model=model),
        'url': f'\'{get_path(model)}\' || id'
    }


def build_queryset(queryset, search_vector, search_query, search_text):
    return queryset.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(
        search=search_text
    ).extra(
        select=build_select_dict(queryset.model)
    ).values('title', 'model_name', 'rank', 'url')


class SearchView(GenericViewSet, ListModelMixin):
    serializer_class = SearchResultSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        city_filter = {'city': user.city} if user.is_authenticated else {}
        SEARCH_QUERYSETS = [
            Article.objects.all(),
            Event.objects.filter(**city_filter, end_at__gt=now()),
            Place.objects.filter(moderation_flag=True, **city_filter),
            Book.objects.all(),
            Movie.objects.all(),
            Video.objects.all(),
            Right.objects.all(),
            Question.objects.exclude(answer=None)
        ]
        search_text = self.request.GET.get('text')
        search_vector = SearchVector('title')
        search_query = SearchQuery(search_text, search_type='plain')
        queryset = Article.objects.none().extra(
            select={
                'model_name': 'null',
                'rank': 'null',
                'url': 'null'
            }
        ).values('title', 'model_name', 'rank', 'url')
        for query in SEARCH_QUERYSETS:
            queryset = queryset.union(
                build_queryset(
                    query,
                    search_vector,
                    search_query,
                    search_text
                )
            )
        return queryset.order_by('-rank')
