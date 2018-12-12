from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

import datetime

from . models import Movie, Preformer, Category, MovieWatchList
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
        self.movie = Movie.objects.create(
            movie_title="Thor: Rangnarok",
            description="Marvel studios, rated M",
        )

        self.actor = Preformer.objects.create(
            name="Chris Hemsworth",
            description="He plays Thor",
            # movies=self.movie
        )
        self.actor.movies.add(self.movie)  # the parent model must be saved first before adding a m2m

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
        self.movie_list = MovieWatchList.objects.create(
            movie_list_name="Felix and Lilyana's favourite movies",
            created_by="A person"
        )

        self.movie = Movie.objects.create(
            movie_title="Thor: Rangnarok",
            description="Lilyana and Felix's favourite",
            recently_added=datetime.date(2018, 1, 1)
        )
        self.movie.movie_lists.add(self.movie_list)

    def test_movie_list_exists(self):
        qs = MovieWatchList.objects.all()
        self.assertEqual(len(qs), 1)

    def test_csrf(self):
        url = reverse('create_movie_watch_list')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_movie_list_valid_post_data(self):
        url = reverse('create_movie_watch_list')
        data = {
            'movie_lists': 'Test title',
            'movie': 'A good movie'
        }
        response = self.client.post(url, data)
        self.assertTrue(MovieWatchList.objects.exists())
        self.assertTrue(Movie.objects.exists())

    def test_new_movie_listc_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('create_movie_watch_list')
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)
