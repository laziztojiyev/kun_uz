from uuid import UUID

import pytest
from django.urls import reverse_lazy, reverse

from reports.models import Region


@pytest.mark.django_db  # check model
class TestRegionView:
    def test_create_region(self):
        region = Region.objects.create(name='Samarqand')
        caunt = Region.objects.count()
        assert region.name == 'Samarqand'
        assert isinstance(region.pk, UUID)
        assert caunt == 1

    def test_create_region_api(self, client):
        url = reverse_lazy('regions-list')
        data = {
            'name': 'Buxoro'
        }
        response = client.post(url, data)
        assert response.data['name'] == data['name']
        assert len(response.data['id']) == 36

    @pytest.fixture
    def regions(self):
        Region.objects.create(name='Toshkent')
        Region.objects.create(name='Samarqand')

    def test_region_api(self, client, regions):
        url = reverse_lazy('regions-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2




