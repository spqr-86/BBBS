from rest_framework import serializers

from ..models import Question
from ..serializers.tag import TagSerializer


class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Question
