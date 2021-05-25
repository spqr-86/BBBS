from rest_framework import permissions, viewsets
from rest_framework.response import Response

from ..models import Main
from ..serializers.main import MainSerializer


class MainViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]

    def list(self, request):
        queryset = Main.objects.order_by('-id').last()
        serializer = MainSerializer(queryset)
        return Response(serializer.data)
