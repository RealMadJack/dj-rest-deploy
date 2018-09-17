from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class GeoHomeTest(TestCase):
    """ Check if External API working """

    def setUp(self):
        pass

    def test_geo_home_template(self):
        geo_home_url = reverse('geo:home')
        resp_client = client.get(geo_home_url)
        self.assertTemplateUsed(resp_client, 'geo_home.html')
