from django.db.models import Count, Exists, F, OuterRef
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from ..filters import EventFilter
from ..models import Event, Participant
from ..permissions import IsUsersCity
from ..serializers import (EventSerializer,
                           ParticipantSerializer, DateEventSerializer)


class ListCreateDelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class Date:
    def __init__(self, months=None):
        self.months = months


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    filter_class = EventFilter

    def get_queryset(self):
        user = self.request.user
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        queryset = Event.objects.filter(city=user.city) \
                        .filter(end_at__gt=now()) \
                        .annotate(booked=Exists(booked)) \
                        .annotate(remain_seats=F('seats')-Count('participants')) \
                        .order_by('-booked', 'start_at')
        return queryset

    @action(methods=['get'], detail=False)
    def months(self, request):
        dates = Event.objects.filter(start_at__gt=now()) \
                              .dates('start_at', 'month')
        months = set([date.month for date in dates])
        date = Date(months=months)
        serializer = DateEventSerializer(date)
        return Response(serializer.data)


class ParticipantViewSet(ListCreateDelViewSet):
    permission_classes = [IsUsersCity, permissions.IsAuthenticated]
    serializer_class = ParticipantSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Participant.objects.filter(participant=self.request.user)

    def create(self, request):
        event = get_object_or_404(Event, id=self.request.data.get('event'))
        self.check_object_permissions(self.request, event)
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(
            Participant, event=pk, participant=request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
