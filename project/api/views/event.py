from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from ..models import Event
from ..permissions import IsUsersCity
from ..serializers import EventSerializer


class EventViewSet(viewsets.ViewSet):
    permission_classes = [IsUsersCity, permissions.IsAuthenticated]

    def list(self, request):
        user = request.user
        booked = Event.objects.filter(pk=OuterRef('pk'), participant=user)
        queryset = Event.objects.filter(
            city=user.profile.city).annotate(
                taken_seats=Count('participant')).annotate(
                    booked=Exists(booked))
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        booked = Event.objects.filter(pk=pk, participant=request.user)
        queryset = Event.objects.annotate(
                taken_seats=Count('participant')).annotate(
                    booked=Exists(booked))
        event = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request, event)
        serializer = EventSerializer(event)
        return Response(serializer.data)
