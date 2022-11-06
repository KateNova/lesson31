import pytest

from tests.factories import CategoryFactory


@pytest.mark.django_db
def test_create_ad(client, user_token):
    CategoryFactory.create_batch(3)
    data = {
        'name': 'testtesttesttest',
        'price': 50,
        'description': 'test description',
        'category': 1,
    }
    response = client.post(
        '/ad/',
        data=data,
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 201
    assert response.data['name'] == data['name']
    assert response.data['price'] == data['price']
    assert response.data['description'] == data['description']
    assert response.data['category'] == data['category']
    assert not response.data['is_published']
    assert isinstance(response.data['author'], int)
