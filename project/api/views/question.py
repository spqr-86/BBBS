from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Question
from ..serializers import QuestionSerializer
from . import GetListPostPutMixin, TagMixin


class QuestionViewSet(GetListPostPutMixin, TagMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filterset_backends = [DjangoFilterBackend]
    filterset_fields = ['tags']
