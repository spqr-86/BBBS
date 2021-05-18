from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def create_users_api(user_client):
    data = {
        'username': 'TestUser1234',
        'role': 'user',
        'email': 'testuser@yamdb.fake'
    }
    user_client.post('/api/v1/users/', data=data)
    user = get_user_model().objects.get(username=data['username'])
    data = {
        'first_name': 'fsdfsdf',
        'last_name': 'dsgdsfg',
        'username': 'TestUser4321',
        'bio': 'Jdlkjd',
        'role': 'moderator',
        'email': 'testuser2342@yamdb.fake'
    }
    user_client.post('/api/v1/users/', data=data)
    moderator = get_user_model().objects.get(username=data['username'])
    return user, moderator


def auth_client(user):
    refresh = RefreshToken.for_user(user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


def create_tags(user_client):
    result = []
    data = {'name': 'Ужасы', 'slug': 'horror'}
    result.append(data)
    user_client.post('/api/v1/tags/', data=data)
    data = {'name': 'Комедия', 'slug': 'comedy'}
    result.append(data)
    user_client.post('/api/v1/tags/', data=data)
    data = {'name': 'Драма', 'slug': 'drama'}
    result.append(data)
    user_client.post('/api/v1/tags/', data=data)
    return result


def create_places(user_client):
    result = []
    data = {
        'title': 'Усадьба',
        'name': 'Имя усадьбы',
        'info': 'Информация о месте Усадьба',
        'description': 'Описание места Усадьба',
        'imageUrl': 'http://somesite.ru/image.png',
        'link': 'http://somesite.ru/',
    }
    response = user_client.post('/api/v1/places/', data=data)
    data['id'] = response.json()['id']
    result.append(data)
    data = {
        'title': 'Полигон',
        'name': 'Имя полигона',
        'info': 'Информация о месте Полигон',
        'description': 'Описание места Полигон',
        'imageUrl': 'http://somesite2.ru/image2.png',
        'link': 'http://somesite2.ru/',
    }
    response = user_client.post('/api/v1/places/', data=data)
    data['id'] = response.json()['id']
    result.append(data)
    return result
