from datetime import date

import pytest


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = 'kate'
    password = '123qwe'
    django_user_model.objects.create_user(
        username=username, 
        password=password, 
        role='member',
        birth_date=date(2000, 1, 1)
    )
    response = client.post(
        '/user/token/',
        {'username': username, 'password': password},
        format='json'
    )
    return response.data['access']
