from django.db.models import Count, Exists, F, OuterRef
from django.utils.timezone import now
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import Event, Main, Place
from ..serializers.main import MainSerializer


def get_event(request):
    user = request.user
    if not user.is_authenticated:
        return None
    booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
    event = Event.objects.filter(end_at__gt=now(), city=user.city) \
                 .annotate(remain_seats=F('seats') - Count('participants')) \
                 .annotate(booked=Exists(booked)) \
                 .order_by('start_at').first()
    return event


def get_place(request):
    user = request.user
    places = Place.objects.all()
    if user.is_authenticated:
        if places.filter(city=user.city).exists():
            return places.filter(city=user.city).last()
    return places.last()


class MainViewSet(RetrieveAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        if instance:
            instance.event = get_event(request)
            instance.place = get_place(request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
