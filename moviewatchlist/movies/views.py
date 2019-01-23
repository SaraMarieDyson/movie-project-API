from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import NewMovieWatchListForm
from .models import Movie, Preformer, MovieWatchList, User


def home(request):
    """Basic home view and redirects to suitable url."""
    return redirect(movie_list)


def movie_list(request):
    """List all individual movies."""
    movies = Movie.objects.all()
    watch_lists = MovieWatchList.objects.all()
    return render(request, "home.html", {"movies": movies, "watch_lists": watch_lists})


def movies_detail(request, pk):
    """View for rendering movie details view."""
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        watch_lists = get_object_or_404(MovieWatchList, pk=pk)
        # Filter list: get actors/actresses who have a movie with this pk.
        # .first(): Get the first performer off the list.
        actor = Preformer.objects.filter(movies__pk=pk)  # .first()
    return render(request, "movie_detail.html", {
                                                "movie": movie,
                                                "actor": actor,
                                                "watch_lists": watch_lists})

def movie_watch_list(request, pk):
    """Retrieve a movie watch list that has been created."""
    if request.method == "GET":
        movie_lists = get_object_or_404(MovieWatchList, pk=pk)
        movies = Movie.objects.filter(movie_lists__pk=movie_lists.pk)
    return render(request, "movie_watch_list.html", {
        "movie_lists": movie_lists, "movies": movies
        })

# NOTE: Get this decorator working properly
# @login_required
def create_movie_watch_list(request):
    """View that allows the user to create a list of movies."""
    user = User.objects.first()
    if request.method == "POST":
        form = NewMovieWatchListForm(request.POST)
        if form.is_valid():
            watch_list = form.save()
            watch_list.created_by = request.user
            return redirect('movie_watch_list', pk=watch_list.pk)
    else:
        form = NewMovieWatchListForm()
    return render(request, "create_movie_watch_list.html", {"form": form})
