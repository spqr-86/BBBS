import pytest

from .common import auth_client, create_places, create_users_api


class TestPlaceAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_place_not_auth(self, client):
        response = client.get('/api/v1/places/')
        assert response.status_code != 404, (
            'Страница `/api/v1/places/` не найдена, проверьте этот адрес в *urls.py*'
        )
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/places/` без токена авторизации возвращается статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_place(self, user_client):
        data = {}
        response = user_client.post('/api/v1/places/', data=data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/api/v1/places/` с не правильными данными возвращает статус 400'
        )
        data = {'title': 'Царское', 'name': 'Село', 'info': 'Информация', 'description': 'Описание', 'imageUrl': 'http://somesite.ru/', 'link': 'http://somesite3.ru/'}
        response = user_client.post('/api/v1/places/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/api/v1/places/` с правильными данными возвращает статус 201'
        )
        data = {'title': 'Село', 'name': 'Царское', 'info': 'Информация 2', 'description': 'Описание 2', 'imageUrl': 'http://somesite2.ru/', 'link': 'http://somesite4.ru/'}
        response = user_client.post('/api/v1/places/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/api/v1/places/` с правильными данными возвращает статус 201'
        )
        response = user_client.get('/api/v1/places/')
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращает статус 200'
        )
        data = response.json()
        assert 'count' in data, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Не найден параметр `count`'
        )
        assert 'next' in data, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Не найден параметр `next`'
        )
        assert 'previous' in data, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Не найден параметр `previous`'
        )
        assert 'results' in data, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Не найден параметр `results`'
        )
        assert data['count'] == 2, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Значение параметра `count` не правильное'
        )
        assert type(data['results']) == list, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Тип параметра `results` должен быть список'
        )
        assert len(data['results']) == 2, (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Значение параметра `results` не правильное'
        )
        assert {'id': 1, 'title': 'Царское', 'name': 'Село', 'info': 'Информация', 'description': 'Описание', 'imageUrl': 'http://somesite.ru/', 'link': 'http://somesite3.ru/'} in data['results'], (
            'Проверьте, что при GET запросе `/api/v1/places/` возвращаете данные с пагинацией. '
            'Значение параметра `results` не правильное'
        )
        response = user_client.get('/api/v1/places/?search=Село')
        data = response.json()
        assert len(data['results']) == 1, (
            'Проверьте, что при GET запросе `/api/v1/places/` фильтуется по search параметру названия места '
        )

    @pytest.mark.django_db(transaction=True)
    def test_03_place_delete(self, user_client):
        places = create_places(user_client)
        response = user_client.delete(f'/api/v1/places/{places[0]["id"]}/')
        assert response.status_code == 204, (
            'Проверьте, что при DELETE запросе `/api/v1/places/{id}/` возвращаете статус 204'
        )
        response = user_client.get('/api/v1/places/')
        test_data = response.json()['results']
        assert len(test_data) == len(places) - 1, (
            'Проверьте, что при DELETE запросе `/api/v1/places/{id}/` удаляете место '
        )
        response = user_client.get(f'/api/v1/places/{places[0]["id"]}/')
        assert response.status_code == 405, (
            'Проверьте, что при GET запросе `/api/v1/places/{id}/` возвращаете статус 405'
        )
        response = user_client.patch(f'/api/v1/places/{places[0]["id"]}/')
        assert response.status_code == 405, (
            'Проверьте, что при PATCH запросе `/api/v1/places/{id}/` возвращаете статус 405'
        )

    def check_permissions(self, user, user_name, places):
        client_user = auth_client(user)
        data = {
            'title': 'Царское село',
            'name': 'Село',
            'info': 'Информация о месте Царское село',
            'description': 'Описание места Царское село',
            'imageUrl': 'http://somesite.ru/image3.png',
            'link': 'http://somesite3.ru/'
        }
        response = client_user.post('/api/v1/places/', data=data)
        assert response.status_code == 403, (
            f'Проверьте, что при POST запросе `/api/v1/places/` '
            f'с токеном авторизации {user_name} возвращается статус 403'
        )
        response = client_user.delete(f'/api/v1/places/{places[0]["id"]}/')
        assert response.status_code == 403, (
            f'Проверьте, что при DELETE запросе `/api/v1/places/{{id}}/` '
            f'с токеном авторизации {user_name} возвращается статус 403'
        )

    @pytest.mark.django_db(transaction=True)
    def test_04_place_check_permission(self, client, user_client):
        places = create_places(user_client)
        data = {
            'title': 'Царское село',
            'name': 'Село',
            'info': 'Информация о месте Царское село',
            'description': 'Описание места Царское село',
            'imageUrl': 'http://somesite.ru/image3.png',
            'link': 'http://somesite3.ru/'
        }
        response = client.post('/api/v1/places/', data=data)
        assert response.status_code == 401, (
            'Проверьте, что при POST запросе `/api/v1/places/` '
            'без токена авторизации возвращается статус 401'
        )
        response = client.delete(f'/api/v1/places/{places[0]["id"]}/')
        assert response.status_code == 401, (
            'Проверьте, что при DELETE запросе `/api/v1/places/{{id}}/` '
            'без токена авторизации возвращается статус 401'
        )
        user, moderator = create_users_api(user_client)
        self.check_permissions(user, 'обычного пользователя', places)
        self.check_permissions(moderator, 'модератора', places)
