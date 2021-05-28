<<<<<<< HEAD
from rest_framework import permissions, viewsets
from rest_framework.response import Response
=======
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
>>>>>>> main

from ..models import Main
from ..serializers.main import MainSerializer


<<<<<<< HEAD
class MainViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
=======
class MainViewSet(ViewSet):
    permission_classes = [AllowAny]
>>>>>>> main

    def list(self, request):
        queryset = Main.objects.order_by('-id').last()
        serializer = MainSerializer(queryset)
        return Response(serializer.data)
