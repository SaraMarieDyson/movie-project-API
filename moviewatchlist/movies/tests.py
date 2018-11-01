from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

from . models import Movie, ActorActressList, Category, MovieWatchList
from . views import home, movies_detail, movie_watch_list

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

    def test_movie_not_found_status_code(self):
        """
        :ac: Returns a 404, if movie doesn't exist
        """
        url = reverse("movies_detail", kwargs={"pk": 99})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_movie_details_resolves_detail_view(self):
        test_movie_detail = resolve("/movies_detail/1/")
        self.assertEqual(test_movie_detail.func, movies_detail)

    def test_movie_detail_contains_information_on_movie(self):
        """
        :ac: Can successfully pull details for a given movie
        """
        url = reverse("movies_detail", kwargs={"pk": self.movie.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

class MovieWatchListTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category="Comedy, Action")
        self.movie_list = MovieWatchList.objects.create(
            movie_list_name="Felix and Lilyana's favourite movies",
            list_of_movies="Thor: Rangnarok",
            created_by="Me"
        )
        self.movie = Movie.objects.create(
            movie_title="Thor: Rangnarok",
            description="Lilyana and Felix's favourite",
            category=self.category,
            movie_list=self.movie_list
        )
        self.actor = ActorActressList.objects.create(name="Chris Hemsworth", description="He plays Thor", movies=self.movie)

    def test_movie_list_resolves_list_view(self):
        """
        :ac: Can resolve list view
        """
        test_movie_list = resolve("/movie_watch_list/1/")
        self.assertEqual(test_movie_list.func, movie_watch_list)
