from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import Main
from ..serializers.main import MainSerializer


class MainViewSet(ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Main.objects.order_by('-id').last()
        serializer = MainSerializer(queryset)
        return Response(serializer.data)
