from ..models import Question
from .base import BaseSerializer


class QuestionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Question
