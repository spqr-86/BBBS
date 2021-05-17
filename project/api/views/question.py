from rest_framework import permissions, viewsets

from ..models import Question
from ..serializers import QuestionSerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
