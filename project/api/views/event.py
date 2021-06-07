from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from ..models import Event, Participant
from ..permissions import IsUsersCity
from ..serializers import EventSerializer, ParticipantSerializer


class ListCreateDelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class EventViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        queryset = Event.objects.filter(city=user.city) \
                                .filter(end_at__gt=now()) \
                                .annotate(booked=Exists(booked)) \
                                .annotate(taken_seats=Count('participants')) \
                                .order_by('start_at')
        return queryset


class ParticipantViewSet(ListCreateDelViewSet):
    permission_classes = [IsUsersCity, permissions.IsAuthenticated]
    serializer_class = ParticipantSerializer
    pagination_class = PageNumberPagination

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
