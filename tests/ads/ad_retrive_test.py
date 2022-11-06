import pytest

from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_retrieve_ad(client, ad):
    response = client.get(f'/ad/{ad.pk}/')

    assert response.status_code == 200
    assert response.data == AdSerializer(ad).data
