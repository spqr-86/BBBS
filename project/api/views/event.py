from django.db.models import Count, F
from rest_framework import permissions, viewsets

from ..models import Event
from ..serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.annotate(taken_seats=Count('participant'))
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
