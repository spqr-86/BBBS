from django.db.models import Count, Exists, F, OuterRef
from django.forms.models import model_to_dict
from django.utils.timezone import now
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from ..models import Event, Main
from ..serializers.main import MainSerializer


def get_events(request):
    user = request.user
    queryset = Event.objects.filter(end_at__gt=now()) \
                    .annotate(remain_seats=F('seats')-Count('participants'))
    if user.is_authenticated:
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        queryset = queryset.filter(city=user.city) \
                           .annotate(booked=Exists(booked))
    return queryset.order_by('start_at')


class MainViewSet(RetrieveAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.last()
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        events = get_events(request)
        main = model_to_dict(instance)
        main['events'] = events
        serializer = self.get_serializer(main)
        return Response(serializer.data)
