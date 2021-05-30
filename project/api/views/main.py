from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView

from ..models import Main
from ..serializers.main import MainSerializer


class MainViewSet(RetrieveAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.last()
        return obj
