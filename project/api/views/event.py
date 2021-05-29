from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from ..models import Event, Participant
from ..permissions import IsUsersCity
from ..serializers import EventSerializer, ParticipantSerializer


class ListCreateDelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class EventViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        city = self.request.query_params.get('city', None)
        queryset = Event.objects.annotate(taken_seats=Count('participants'))
        if user.is_anonymous:
            if city is not None:
                queryset = queryset.filter(city=city)
            return queryset.order_by('start_at')
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        queryset = queryset.annotate(
            booked=Exists(booked)).filter(city=user.city)
        return queryset.order_by('start_at')


class ParticipantViewSet(ListCreateDelViewSet):
    permission_classes = [IsUsersCity, permissions.IsAuthenticated]
    serializer_class = ParticipantSerializer
    pagination_class = None

    def get_queryset(self):
        return Participant.objects.filter(participant=self.request.user)

    def create(self, request):
        event = get_object_or_404(Event, id=self.request.POST.get('event'))
        self.check_object_permissions(self.request, event)
        serializer = self.get_serializer(data=self.request.POST)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(
            Participant, event=pk, participant=request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
