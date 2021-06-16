from rest_framework.serializers import Serializer

from ..serializers import (ArticleSerializer, HistorySerializer,
                           MainEventSerializer, MovieSerializer,
                           PlaceSerializer, QuestionSerializer,
                           VideoSerializer)


class MainSerializer(Serializer):
    event = MainEventSerializer(required=False, read_only=True)
    history = HistorySerializer(required=False, read_only=True)
    place = PlaceSerializer(required=False, read_only=True)
    articles = ArticleSerializer(many=True, required=False, read_only=True)
    movies = MovieSerializer(many=True, required=False, read_only=True)
    video = VideoSerializer(required=False, read_only=True)
    questions = QuestionSerializer(many=True, required=False, read_only=True)
