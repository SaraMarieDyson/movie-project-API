from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

from . models import Movie, ActorActressList

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


class MovieDetailsViewTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(movie_title="Thor: Rangnarok", description="Lilyana and Felix's favourite")
        self.actor = ActorActressList.objects.create(name="Chris Hemsworth", description="He plays Thor", movies=self.movie)

    def test_movie_detail_status_code(self):
        """
        :ac: Returns a status 200
        """
        url = reverse("movies_detail", kwargs={"pk": self.movie.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
