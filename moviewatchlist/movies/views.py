from django.shortcuts import render, get_object_or_404
from . models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movies_detail(request, pk):
    movies = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_detail.html", {"movies": movies})
