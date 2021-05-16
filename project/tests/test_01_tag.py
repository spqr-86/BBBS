import pytest

from .common import auth_client, create_tag, create_users_api


class TestTagAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_tag_not_auth(self, client):
        response = client.get('/api/v1/tags/')
        assert response.status_code != 404, (
            'Страница `/api/v1/tags/` не найдена, проверьте этот адрес в *urls.py*'
        )
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/tags/` без токена авторизации возвращается статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_02_tag(self, user_client):
        data = {}
        response = user_client.post('/api/v1/tags/', data=data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/api/v1/tags/` с не правильными данными возвращает статус 400'
        )
        data = {'name': 'Ужасы', 'slug': 'horror'}
        response = user_client.post('/api/v1/tags/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/api/v1/tags/` с правильными данными возвращает статус 201'
        )
        data = {'name': 'Триллер', 'slug': 'horror'}
        response = user_client.post('/api/v1/tags/', data=data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе `/api/v1/tags/` нельзя создать 2 категории с одинаковым `slug`'
        )
        data = {'name': 'Комедия', 'slug': 'comedy'}
        response = user_client.post('/api/v1/tags/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/api/v1/tags/` с правильными данными возвращает статус 201'
        )
        response = user_client.get('/api/v1/tags/')
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращает статус 200'
        )
        data = response.json()
        assert 'count' in data, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Не найден параметр `count`'
        )
        assert 'next' in data, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Не найден параметр `next`'
        )
        assert 'previous' in data, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Не найден параметр `previous`'
        )
        assert 'results' in data, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Не найден параметр `results`'
        )
        assert data['count'] == 2, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Значение параметра `count` не правильное'
        )
        assert type(data['results']) == list, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Тип параметра `results` должен быть список'
        )
        assert len(data['results']) == 2, (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Значение параметра `results` не правильное'
        )
        assert {'name': 'Ужасы', 'slug': 'horror'} in data['results'], (
            'Проверьте, что при GET запросе `/api/v1/tags/` возвращаете данные с пагинацией. '
            'Значение параметра `results` не правильное'
        )
        response = user_client.get('/api/v1/tags/?search=Ужасы')
        data = response.json()
        assert len(data['results']) == 1, (
            'Проверьте, что при GET запросе `/api/v1/tags/` фильтуется по search параметру названия тега '
        )

    @pytest.mark.django_db(transaction=True)
    def test_03_tag_delete(self, user_client):
        tags = create_tag(user_client)
        response = user_client.delete(f'/api/v1/tags/{tags[0]["slug"]}/')
        assert response.status_code == 204, (
            'Проверьте, что при DELETE запросе `/api/v1/tags/{slug}/` возвращаете статус 204'
        )
        response = user_client.get('/api/v1/tags/')
        test_data = response.json()['results']
        assert len(test_data) == len(tags) - 1, (
            'Проверьте, что при DELETE запросе `/api/v1/tags/{slug}/` удаляете категорию '
        )
        response = user_client.get(f'/api/v1/tags/{tags[0]["slug"]}/')
        assert response.status_code == 405, (
            'Проверьте, что при GET запросе `/api/v1/tags/{slug}/` возвращаете статус 405'
        )
        response = user_client.patch(f'/api/v1/tags/{tags[0]["slug"]}/')
        assert response.status_code == 405, (
            'Проверьте, что при PATCH запросе `/api/v1/tags/{slug}/` возвращаете статус 405'
        )

    def check_permissions(self, user, user_name, tags):
        client_user = auth_client(user)
        data = {
            'name': 'Боевик',
            'slug': 'action'
        }
        response = client_user.post('/api/v1/tags/', data=data)
        assert response.status_code == 403, (
            f'Проверьте, что при POST запросе `/api/v1/tags/` '
            f'с токеном авторизации {user_name} возвращается статус 403'
        )
        response = client_user.delete(f'/api/v1/tags/{tags[0]["slug"]}/')
        assert response.status_code == 403, (
            f'Проверьте, что при DELETE запросе `/api/v1/tags/{{slug}}/` '
            f'с токеном авторизации {user_name} возвращается статус 403'
        )

    @pytest.mark.django_db(transaction=True)
    def test_04_tag_check_permission(self, client, user_client):
        tags = create_tag(user_client)
        data = {
            'name': 'Боевик',
            'slug': 'action'
        }
        response = client.post('/api/v1/tags/', data=data)
        assert response.status_code == 401, (
            'Проверьте, что при POST запросе `/api/v1/tags/` '
            'без токена авторизации возвращается статус 401'
        )
        response = client.delete(f'/api/v1/tags/{tags[0]["slug"]}/')
        assert response.status_code == 401, (
            'Проверьте, что при DELETE запросе `/api/v1/tags/{{slug}}/` '
            'без токена авторизации возвращается статус 401'
        )
        user, moderator = create_users_api(user_client)
        self.check_permissions(user, 'обычного пользователя', tags)
        self.check_permissions(moderator, 'модератора', tags)
