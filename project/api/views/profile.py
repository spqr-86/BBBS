from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, viewsets

from ..models import Profile
from ..serializers import ProfileSerializer

User = get_user_model()


class RetrieveUpdateViewSet(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    pass


class ProfileViewSet(RetrieveUpdateViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
