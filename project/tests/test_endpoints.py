import pytest


class TestAccountApi:
    @pytest.mark.django_db(transaction=True)
    def test_token_obtain_pair(self, client):
        response = client.get('/api/v1/token/')
        assert response.status_code != 404, (
            'Страница `/api/v1/token/` не найдена, проверьте этот адрес в *urls.py*'
        )

    @pytest.mark.django_db(transaction=True)
    def test_token_refresh(self, client):
        response = client.get('/api/v1/token/refresh/')
        assert response.status_code != 404, (
            'Страница `/api/v1/token/refresh/` не найдена, проверьте этот адрес в *urls.py*'
        )


class TestArticleAPI:
    @pytest.mark.django_db(transaction=True)
    def test_article_not_found(self, client, ):
        response = client.get('/api/v1/articles/')

        assert response.status_code != 404, 'Страница `/api/v1/articles/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_article_not_auth(self, client, ):
        response = client.get('/api/v1/articles/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/articles/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_article_get(self, user_client, ):
        response = user_client.get('/api/v1/articles/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/articles/` с токеном авторизации возвращаетсся статус 200'


class TestBookAPI:
    @pytest.mark.django_db(transaction=True)
    def test_book_not_found(self, client, ):
        response = client.get('/api/v1/books/')

        assert response.status_code != 404, 'Страница `/api/v1/books/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_book_not_auth(self, client, ):
        response = client.get('/api/v1/books/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/books/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_book_get(self, user_client, ):
        response = user_client.get('/api/v1/books/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/books/` с токеном авторизации возвращаетсся статус 200'


class TestCatalogAPI:
    @pytest.mark.django_db(transaction=True)
    def test_catalog_not_found(self, client, ):
        response = client.get('/api/v1/catalog/')

        assert response.status_code != 404, 'Страница `/api/v1/catalog/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_catalog_not_auth(self, client, ):
        response = client.get('/api/v1/catalog/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/catalog/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_catalog_get(self, user_client, ):
        response = user_client.get('/api/v1/catalog/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/catalog/` с токеном авторизации возвращаетсся статус 200'


class TestHistoryAPI:
    @pytest.mark.django_db(transaction=True)
    def test_history_not_found(self, client, ):
        response = client.get('/api/v1/history/')

        assert response.status_code != 404, 'Страница `/api/v1/history/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_history_not_auth(self, client, ):
        response = client.get('/api/v1/history/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/history/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_history_get(self, user_client, ):
        response = user_client.get('/api/v1/history/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/history/` с токеном авторизации возвращаетсся статус 200'


class TestPlaceAPI:
    @pytest.mark.django_db(transaction=True)
    def test_place_not_found(self, client, ):
        response = client.get('/api/v1/places/')

        assert response.status_code != 404, 'Страница `/api/v1/places/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_place_not_auth(self, client, ):
        response = client.get('/api/v1/places/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/places/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_place_get(self, user_client, ):
        response = user_client.get('/api/v1/places/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/places/` с токеном авторизации возвращаетсся статус 200'


class TestTagAPI:
    @pytest.mark.django_db(transaction=True)
    def test_tag_not_found(self, client, ):
        response = client.get('/api/v1/tags/')

        assert response.status_code != 404, 'Страница `/api/v1/tags/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_tag_not_auth(self, client, ):
        response = client.get('/api/v1/tags/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/tags/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_tag_get(self, user_client, ):
        response = user_client.get('/api/v1/tags/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/tags/` с токеном авторизации возвращаетсся статус 200'


class TestRightAPI:
    @pytest.mark.django_db(transaction=True)
    def test_tag_not_found(self, client, ):
        response = client.get('/api/v1/rights/')

        assert response.status_code != 404, 'Страница `/api/v1/rights/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_tag_not_auth(self, client, ):
        response = client.get('/api/v1/rights/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/rights/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_tag_get(self, user_client, ):
        response = user_client.get('/api/v1/rights/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/rights/` с токеном авторизации возвращаетсся статус 200'


class TestMovieAPI:
    @pytest.mark.django_db(transaction=True)
    def test_movie_not_found(self, client, ):
        response = client.get('/api/v1/movies/')

        assert response.status_code != 404, 'Страница `/api/v1/movies/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_movie_not_auth(self, client, ):
        response = client.get('/api/v1/movies/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/movies/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_movie_get(self, user_client, ):
        response = user_client.get('/api/v1/movies/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/movies/` с токеном авторизации возвращаетсся статус 200'


class TestVideoAPI:
    @pytest.mark.django_db(transaction=True)
    def test_video_not_found(self, client, ):
        response = client.get('/api/v1/videos/')

        assert response.status_code != 404, 'Страница `/api/v1/videos/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_video_not_auth(self, client, ):
        response = client.get('/api/v1/videos/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/videos/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_video_get(self, user_client, ):
        response = user_client.get('/api/v1/videos/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/videos/` с токеном авторизации возвращаетсся статус 200'


class TestQuestionAPI:
    @pytest.mark.django_db(transaction=True)
    def test_question_not_found(self, client, ):
        response = client.get('/api/v1/questions/')

        assert response.status_code != 404, 'Страница `/api/v1/questions/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_question_not_auth(self, client, ):
        response = client.get('/api/v1/questions/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/questions/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_question_get(self, user_client, ):
        response = user_client.get('/api/v1/questions/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/questions/` с токеном авторизации возвращаетсся статус 200'


class TestCityAPI:
    @pytest.mark.django_db(transaction=True)
    def test_city_not_found(self, client, ):
        response = client.get('/api/v1/cities/')

        assert response.status_code != 404, 'Страница `/api/v1/cities/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_city_not_auth(self, client, ):
        response = client.get('/api/v1/cities/')

        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/cities/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_city_get(self, user_client, ):
        response = user_client.get('/api/v1/cities/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/cities/` с токеном авторизации возвращаетсся статус 200'


class TestDiaryAPI:
    @pytest.mark.django_db(transaction=True)
    def test_diary_not_found(self, client, ):
        response = client.get('/api/v1/profile/diaries/')

        assert response.status_code != 404, 'Страница `/api/v1/profile/diaries/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_diary_not_auth(self, client, ):
        response = client.get('/api/v1/profile/diaries/')

        assert response.status_code == 401,\
            'Проверьте, что `/api/v1/profile/diaries/` при запросе без токена возвращаете статус 401'

    @pytest.mark.django_db(transaction=True)
    def test_diary_get(self, user_client, ):
        response = user_client.get('/api/v1/profile/diaries/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/profile/diaries/` с токеном авторизации возвращаетсся статус 200'


class TestEventAPI:
    @pytest.mark.django_db(transaction=True)
    def test_event_not_found(self, client, ):
        response = client.get('/api/v1/afisha/events/')

        assert response.status_code != 404, 'Страница `/api/v1/afisha/events/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_event_not_auth(self, client, ):
        response = client.get('/api/v1/afisha/events/')

        assert response.status_code == 401,\
            'Проверьте, что `/api/v1/afisha/events/` при запросе без токена возвращаете статус 401'

    @pytest.mark.django_db(transaction=True)
    def test_event_get(self, user_client, ):
        response = user_client.get('/api/v1/afisha/events/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/afisha/events/` с токеном авторизации возвращаетсся статус 200'


class TestEventParticipantArchiveAPI:
    @pytest.mark.django_db(transaction=True)
    def test_archive_not_found(self, client, ):
        response = client.get('/api/v1/afisha/event-participants/archive/')

        assert response.status_code != 404, 'Страница `/api/v1/afisha/event-participants/archive/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_archive_not_auth(self, client, ):
        response = client.get('/api/v1/afisha/event-participants/archive/')

        assert response.status_code == 401,\
            'Проверьте, что `/api/v1/afisha/event-participants/archive/` при запросе без токена возвращаете статус 401'

    @pytest.mark.django_db(transaction=True)
    def test_archive_get(self, user_client, ):
        response = user_client.get('/api/v1/afisha/event-participants/archive/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/afisha/event-participants/archive/` с токеном авторизации возвращаетсся статус 200'


class TestEventParticipantAPI:
    @pytest.mark.django_db(transaction=True)
    def test_participant_not_found(self, client, ):
        response = client.get('/api/v1/afisha/event-participants/')

        assert response.status_code != 404, 'Страница `/api/v1/afisha/event-participants/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_participant_not_auth(self, client, ):
        response = client.get('/api/v1/afisha/event-participants/')

        assert response.status_code == 401,\
            'Проверьте, что `/api/v1/afisha/event-participants/` при запросе без токена возвращаете статус 401'

    @pytest.mark.django_db(transaction=True)
    def test_participant_get(self, user_client, ):
        response = user_client.get('/api/v1/afisha/event-participants/')

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/afisha/event-participants/` с токеном авторизации возвращаетсся статус 200'
