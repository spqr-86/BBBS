from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers import ProfileSerializer
from ..utils.BaseViewSet import BaseAttendersView
from ..utils.email import send_email
from ...account.models import CustomUser

User = get_user_model()


class ProfileViewSet(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class SendMailViewSet(BaseAttendersView):
    permission_classes_by_action = {
        'send_password': [AllowAny]
    }

    @method_decorator(csrf_exempt)
    def send_password(self, request: Request):
        email = self.request.query_params['email']
        user = CustomUser.objects.get(email=email)
        send_email([user.email], 'password', user.password)
        return Response({'sent': 'true'})
