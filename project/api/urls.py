from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

v1_router = DefaultRouter()

v1_router.register(r'articles', views.ArticleViewSet, basename='article')
v1_router.register(r'books', views.BookView, basename='book')
v1_router.register(r'catalog', views.CatalogView, basename='catalog')
v1_router.register(r'history', views.HistoryViewSet, basename='history')
v1_router.register(r'places', views.PlacesViewSet, basename='places')
v1_router.register(r'tags', views.TagViewSet, basename='tag')
v1_router.register(r'rights', views.RightViewSet, basename='right')
v1_router.register(r'movies', views.MovieView, basename='movies')
v1_router.register(r'videos', views.VideoView, basename='videos')
v1_router.register(r'questions', views.QuestionViewSet, basename='questions')
v1_router.register(r'cities', views.CityViewSet, basename='city')
v1_router.register(r'profile/diaries', views.DiaryViewSet, basename='diary')
v1_router.register(r'afisha/events', views.EventViewSet, basename='event')
v1_router.register(r'afisha/event-participants',
                   views.ParticipantViewSet,
                   basename='event-participant')
v1_router.register(r'events-participant/archive',
                   views.MyEventsArchive,
                   basename='my-events-archive')

app_name = 'api'

urlpatterns = [
    path(
        'v1/main/',
        views.MainViewSet.as_view(), name='main'
    ),
    path(
        'v1/profile/',
        views.ProfileViewSet.as_view(), name='profile'
    ),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('v1/', include((v1_router.urls, 'v1'), namespace='v1')),
]
