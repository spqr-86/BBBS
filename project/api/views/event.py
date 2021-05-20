from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from ..models import Event
from ..serializers import EventSerializer


class EventViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user = request.user
        queryset = Event.objects.filter(
            city=user.profile.city).annotate(
                taken_seats=Count('participant'))
        serializer = EventSerializer(
            queryset, many=True, context={'user': user})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = request.user
        queryset = Event.objects.annotate(taken_seats=Count('participant'))
        event = get_object_or_404(queryset, pk=pk, city=user.profile.city)
        serializer = EventSerializer(event, context={'user': request.user})
        return Response(serializer.data)
