from django.db.models import Count, Exists, F, OuterRef
from django.utils.timezone import now
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import Article, Event, History, Movie, Place, Question, Video
from ..serializers.main import MainSerializer
from ..utils.castraitor import Castraitor


class MainPage:
    def __init__(self, event=None, history=None, place=None,
                 articles=None, movies=None, video=None, questions=None):
        self.event = event
        self.history = history
        self.place = place
        self.articles = articles
        self.movies = movies
        self.video = video
        self.questions = questions


def get_event(request):
    user = request.user
    if not user.is_authenticated:
        return None
    booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
    events = Event.objects.filter(end_at__gt=now(), city=user.city) \
                  .annotate(booked=Exists(booked)) \
                  .annotate(remain_seats=F('seats') - Count('participants'))
    return events.order_by('start_at').first()


def get_place(request):
    user = request.user
    city = request.data.get('city')
    places = Place.objects.filter(output_to_main=True)
    if user.is_authenticated:
        if places.filter(city=user.city).exists():
            return places.filter(city=user.city).last()
        return places.last()
    if city is not None:
        if places.filter(city=city).exists():
            return places.filter(city=city).last()
    return places.last()


class MainViewSet(RetrieveAPIView):
    serializer_class = MainSerializer
    permission_classes = [AllowAny]

    MOVIES_LENGTH = 7
    QUESTION_LENGTH = 10
    ARTICLES_LENGTH = 2

    def retrieve(self, request, *args, **kwargs):
        instance = MainPage()
        instance.event = get_event(request)
        instance.history = History.objects.filter(output_to_main=True).last()
        instance.place = get_place(request)
        instance.articles = Castraitor(Article, self.ARTICLES_LENGTH, '-id').get_n_records()
        instance.movies = Castraitor(Movie, self.MOVIES_LENGTH, '-id').get_n_records()
        instance.video = Video.objects.filter(output_to_main=True).last()
        instance.questions = Castraitor(Question, self.QUESTION_LENGTH, '-id').get_n_records()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
