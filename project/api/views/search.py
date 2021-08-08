# Статьи, События, Места, Книги, Видео, Фильмы, Права, Вопросы
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from django.contrib.postgres.search import (SearchVector, SearchQuery,
                                            SearchRank)

from ..models import Article, Event, Place, Book, Movie, Video, Right, Question
from ..serializers import SearchResultSerializer

SEARCH_MODELS = [Event, Place, Book, Movie, Video, Right, Question]
SELECT_VALUE = "'{model._meta.verbose_name_plural}'"


def build_select_dict(model):
    return {'model_name': SELECT_VALUE.format(model=model)}


def build_queryset(model, search_vector, search_query, search_text):
    return model.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(
        search=search_text
    ).extra(
        select=build_select_dict(model)
    ).values('title', 'model_name', 'rank')


class SearchView(GenericViewSet, ListModelMixin):
    serializer_class = SearchResultSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        search_text = self.request.GET.get('text')
        search_vector = SearchVector('title')
        search_query = SearchQuery(search_text, search_type='plain')
        queryset = build_queryset(
            Article,
            search_vector,
            search_query,
            search_text
        )
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
