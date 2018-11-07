from django.shortcuts import render, get_object_or_404
from . models import Movie, ActorActressList, MovieWatchList


def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movies_detail(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        # Filter list: get actors/actresses who have a movie with this pk.
        # .first(): Get the first performer off the list.
        actor = ActorActressList.objects.filter(movies__pk=pk).first()
    return render(request, "movie_detail.html", {"movie": movie, "actor": actor})

def movie_watch_list(request, pk):
    movie_list = get_object_or_404(MovieWatchList, pk=pk)
    return render(request, "movie_watch_list.html", {"movie_list": movie_list})
