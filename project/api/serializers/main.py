from rest_framework.serializers import Serializer

from ..models import Main
from ..serializers import (ArticleSerializer, MainEventSerializer,
                           HistorySerializer, MovieSerializer, PlaceSerializer,
                           QuestionSerializer, VideoSerializer)


class MainSerializer(Serializer):
    events = MainEventSerializer(many=True, required=False, read_only=True)
    histories = HistorySerializer(many=True, required=False, read_only=True)
    places = PlaceSerializer(many=True, required=False, read_only=True)
    articles = ArticleSerializer(many=True, required=False, read_only=True)
    movies = MovieSerializer(many=True, required=False, read_only=True)
    video = VideoSerializer(many=True, required=False, read_only=True)
    questions = QuestionSerializer(many=True, required=False, read_only=True)

    class Meta:
        exclude = ['id', 'title']
        model = Main
