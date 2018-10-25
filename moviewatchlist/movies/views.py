from django.shortcuts import render, get_object_or_404
from . models import Movie, ActorActressList

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movies_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    lead = get_object_or_404(ActorActressList, pk=pk)
    try:
        movie = Movie.objects.get(pk=pk)
        lead_in_movie = ActorActressList.objects.filter(movies__movie_title=lead)
    except Movie.DoesNotExist:
        raise Http404
    return render(request, "movie_detail.html", {"movie": movie})
    # if request.method == "GET":
    #     movie_info = get_object_or_404(Movie, pk=pk)
    #     lead = ActorActressList.objects.get(pk=pk)
    #     lead_in_movie = ActorActressList.objects.filter(movies__movie_title=lead)
    # return render(request, "movie_detail.html",)
    # return render(request, "movie_detail.html", {"movies": movies, "actor": actor})
