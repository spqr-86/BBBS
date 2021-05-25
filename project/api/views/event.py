from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from ..models import Event, Participant
from ..permissions import IsUsersCity
from ..serializers import (EventSerializer,
                           ParticipantReadSerializer,
                           ParticipantWriteSerializer)


class ListCreateDelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class EventViewSet(viewsets.ViewSet):
    permission_classes = [IsUsersCity, permissions.IsAuthenticated]

    def list(self, request):
        user = request.user
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        queryset = Event.objects.filter(
            city=user.profile.city).annotate(
                taken_seats=Count('participants')).annotate(
                    booked=Exists(booked))
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        booked = Event.objects.filter(pk=pk, participants=request.user)
        queryset = Event.objects.annotate(
                taken_seats=Count('participants')).annotate(
                    booked=Exists(booked))
        event = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request, event)
        serializer = EventSerializer(event)
        return Response(serializer.data)


class ParticipantViewSet(ListCreateDelViewSet):
    permission_classes = [IsUsersCity, permissions.IsAuthenticated]
    serializer_class = ParticipantReadSerializer
    pagination_class = None

    def get_queryset(self):
        return Participant.objects.filter(participant=self.request.user)

    def create(self, request):
        event = get_object_or_404(Event, id=self.request.data.get('event'))
        self.check_object_permissions(self.request, event)
        self.request.data['participant'] = request.user.id
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(
            Participant, event=pk, participant=request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParticipantReadSerializer
        return ParticipantWriteSerializer
