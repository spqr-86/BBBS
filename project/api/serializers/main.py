from rest_framework.serializers import ModelSerializer

from ..models import Main
<<<<<<< HEAD
from ..serializers import (EventSerializer,
                           HistorySerializer,
                           PlaceSerializer,
                           ArticleSerializer,
                           MovieSerializer,
                           VideoSerializer,
                           QuestionSerializer)
=======
from ..serializers import (ArticleSerializer, EventSerializer,
                           HistorySerializer, MovieSerializer, PlaceSerializer,
                           QuestionSerializer, VideoSerializer)
>>>>>>> main


class MainSerializer(ModelSerializer):
    events = EventSerializer(many=True, required=False, read_only=True)
    histories = HistorySerializer(many=True, required=False, read_only=True)
    places = PlaceSerializer(many=True, required=False, read_only=True)
    articles = ArticleSerializer(many=True, required=False, read_only=True)
    movies = MovieSerializer(many=True, required=False, read_only=True)
    video = VideoSerializer(many=True, required=False, read_only=True)
    questions = QuestionSerializer(many=True, required=False, read_only=True)

    class Meta:
        exclude = ['id', 'title']
        model = Main
