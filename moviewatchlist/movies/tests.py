from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

from . models import Movie

class HomePageTests(TestCase):
    def setUp(self):
        Movie.objects.create(movie_title="Test movie", description="testing 123")

    def test_home_view_staus_code(self):
        """
        :ac: Returns a status 200
        """
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
