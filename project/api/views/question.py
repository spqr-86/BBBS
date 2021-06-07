from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Question, Tag
from ..serializers import QuestionSerializer
from .tag import TagSerializer


class QuestionViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filterset_backends = [DjangoFilterBackend]
    filterset_fields = ['tags']

    @action(methods=['get'], detail=False)
    def tags(self, request):
        tags = Tag.objects.filter(questions__isnull=False)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
