from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewMovieWatchListForm
from .models import Movie, Preformer, MovieWatchList


def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})

def movies_detail(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        # Filter list: get actors/actresses who have a movie with this pk.
        # .first(): Get the first performer off the list.
        actor = Preformer.objects.filter(movies__pk=pk)  #.first()
    return render(request, "movie_detail.html", {"movie": movie, "actor": actor})

def movie_watch_list(request, pk):
    if request.method == "GET":
        movie_lists = get_object_or_404(MovieWatchList, pk=pk)
        movies = Movie.objects.filter(movie_lists__pk=pk)
    return render(request, "movie_watch_list.html", {"movie_lists": movie_lists, "movies": movies})

def create_movie_watch_list(request):
    # Happy path
    if request.method == "POST":
        form = NewMovieWatchListForm(request.POST)
        if form.is_valid():
            watch_list = form.save(commit=False)
            watch_list.movie_list_name = request.movie_list_name
            watch_list.list_created = request.created_by
            # watch_list.list_created = timezone.now
            watch_list.save()

            movie_lists = MovieWatchList.objects.create(
                movie_list_name=movie_list_name,
                list_created=list_created,
                created_by=created_by
            )

            movie = Movie.objects.create(
                movie_title=movies,
                movie_list=watch_list
            )
            # return redirect('movie_lists') # , pk=movie_list.pk)  # TODO: redirect to the created list
    else:
        form = NewMovieWatchListForm()
    return render(request, "create_movie_watch_list.html", {"form": form})
