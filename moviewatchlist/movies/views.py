from django.shortcuts import render, get_object_or_404
from . models import Movie, ActorActressList

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movies_detail(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        # movie_id = Movie.objects.get(pk=id)
        # Filter list: get actors/actresses who have a movie with this pk.
        # .first(): Get the first performer off the list.
        actor = ActorActressList.objects.filter(movies__pk=pk).first()
        # try:
        #     movie = Movie.objects.get(pk=pk)
        #     lead_in_movie = ActorActressList.objects.filter(movies__movie_title=lead)
        # except Movie.DoesNotExist:
        #     raise Http404
    return render(request, "movie_detail.html", {"movie": movie, "actor": actor})
    # return render(request, "movie_detail.html", {"movie": movie})
