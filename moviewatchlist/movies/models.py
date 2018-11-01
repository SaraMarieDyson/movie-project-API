from django.db import models
from django.contrib.auth.models import User # Using the django built in user for now


class MovieWatchList(models.Model):
    """
    Stores a list of movies
    """
    movie_list_name = models.CharField(max_length=100, help_text="The title of the list")
    list_of_movies = models.TextField(null=True)
    list_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, help_text="The unregistered User's name")


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
    movie_title = models.CharField(max_length=100, help_text="names a movie's title")
    description = models.CharField(max_length=200, help_text="details about a movie, such as ratings, release etc")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="movie_category")
    movie_list = models.ForeignKey(MovieWatchList, on_delete=models.CASCADE, blank=True, null=True, related_name="movie_list")

    def __str__(self):
        return self.movie_title

    # @property
    # def movie_list(self):
    #     # Watch for large querysets: it loads everything in memory
    #     # This is useful for if movie_list is set as ManyToManyField
    #     return list(self.movie_list.all())


class ActorActressList(models.Model):
    """
    A Actor/Actress list for movie app and links them to the movie and review models
    """
    name = models.CharField(max_length=50, help_text="name of the preformer")
    description = models.CharField(max_length=200, help_text="gives information about the preformer")
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="actor_actress_list")
    # NOTE: FK may need a many to many relationship on this ^


class Review(models.Model):
    """
    A review model so reiews can be left for movies and actors/actresses
    """
    review_title = models.CharField(max_length=50, help_text="A title for the review")
    review = models.TextField(max_length=5000, help_text="The body of the review")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    actor_actress = models.ForeignKey(ActorActressList, on_delete=models.CASCADE, related_name="review")
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
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="post")
