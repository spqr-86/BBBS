from .base import BaseSerializer
from ..models import Question


class QuestionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Question
