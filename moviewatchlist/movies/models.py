from django.db import models
from django.contrib.auth.models import User # Using the django built in user for now


class MovieWatchList(models.Model):
    """
    Stores a list of movies
    """
    movie_list_name = models.CharField(max_length=100, help_text="The title of the list", blank=True)
    list_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, help_text="The unregistered User's name")

    def __str__(self):
        return self.movie_list_name


class Category(models.Model):
    """
    Lists the Category or genre of the movie ie Action, RomCom, Drama
    """
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Movie(models.Model):
    """
    A movie model for listing movie titles and a description
    """
    movie_title = models.CharField(max_length=300, help_text="names a movie's title")
    description = models.CharField(max_length=500, help_text="details about a movie, such as ratings, release etc")
    movie_lists = models.ManyToManyField(MovieWatchList, related_name="movie_list", blank=True)
    recently_added = models.DateTimeField("Created time", auto_now_add=True, null=True)

    class Meta:
        get_latest_by = "recently_added"

    def __str__(self):
        return self.movie_title


class Preformer(models.Model):
    """
    An Actor/Actress list for movie app and links them to the movie and review models
    """
    name = models.CharField(max_length=300, help_text="name of the preformer")
    description = models.CharField(max_length=500, help_text="gives information about the preformer")
    movies = models.ManyToManyField(Movie, related_name="movie")

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    A review model so reiews can be left for movies and actors/actresses
    """
    review_title = models.CharField(max_length=50, help_text="A title for the review")
    review = models.TextField(max_length=5000, help_text="The body of the review")
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    preformers = models.ForeignKey(Preformer, on_delete=models.CASCADE, related_name="review", null=True)
    authored_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    """
    A model class that allow users to post messages below a review
    """
    message = models.TextField(max_length=1000, help_text="Posts made by users below a review")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="post")
