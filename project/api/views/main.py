from django.db.models import Count, Exists, F, OuterRef
from django.utils.timezone import now
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import Event, Main, Place
from ..serializers.main import MainSerializer


def get_event(request):
    user = request.user
    city = request.data.get('city')
    events = Event.objects.filter(end_at__gt=now()) \
                  .annotate(remain_seats=F('seats') - Count('participants'))
    if user.is_authenticated:
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        events = events.filter(city=user.city).annotate(booked=Exists(booked))
        return events.order_by('start_at').first()
    if city is not None:
        events = events.filter(city=city)
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
