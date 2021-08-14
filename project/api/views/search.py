from django.contrib.postgres.search import (SearchVector, SearchQuery,
                                            SearchRank)
from django.urls import reverse
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ..models import Article, Event, Place, Book, Movie, Video, Right, Question
from ..serializers import SearchResultSerializer

SEARCH_MODELS = [Event, Place, Book, Movie, Video, Right, Question]
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


def build_queryset(model, search_vector, search_query, search_text):
    return model.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(
        search=search_text
    ).extra(
        select=build_select_dict(model)
    ).values('title', 'model_name', 'rank', 'url')


class SearchView(GenericViewSet, ListModelMixin):
    serializer_class = SearchResultSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
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
        for model in SEARCH_MODELS:
            queryset = queryset.union(
                build_queryset(
                    model,
                    search_vector,
                    search_query,
                    search_text
                )
            )
        return queryset.order_by('-rank')
