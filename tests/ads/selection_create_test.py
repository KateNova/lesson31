import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_list_ad(client, user_token):
    ads = AdFactory.create_batch(10)
    ad_ids = [x.id for x in ads]
    data = {
        'name': 'test',
        'items': ad_ids
    }
    response = client.post(
        '/selection/',
        data=data,
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 201
    assert response.data['name'] == data['name']
    assert response.data['items'] == ad_ids
