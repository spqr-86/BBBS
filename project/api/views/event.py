from rest_framework import permissions, viewsets

from ..models import Event, Profile
from ..serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get_queryset(self):
        if self.request.user:
            events = Event.objects.filter(
                city=Profile.city(user=self.request.user)
            )
        else:
            events = Event.objects.filter(city=self.kwargs.get('city'))
        return events

    def perform_create(self, serializer):
        serializer.save()
