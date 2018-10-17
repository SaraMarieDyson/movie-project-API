from django.shortcuts import render, get_object_or_404
from . models import Movie, ActorActressList

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
