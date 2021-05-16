from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import *

v1_router = DefaultRouter()

v1_router.register(r'places', PlaceViewSet, basename='place')
v1_router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
