from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404

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
            profile = get_object_or_404(Profile, user=self.request.user)
            events = Event.objects.filter(
                city=profile.city
            )
        else:
            events = Event.objects.filter(city=self.kwargs.get('city'))
        return events

    def perform_create(self, serializer):
        serializer.save()
