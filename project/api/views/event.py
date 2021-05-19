from django.db.models import Count, F, Case, When, Exists
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from ..models import Event
from ..serializers import EventSerializer


class EventViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Event.objects.annotate(taken_seats=Count('participant'))
        serializer = EventSerializer(
            queryset, many=True, context={'user': request.user})
        return Response(serializer.data)
