from django import forms
from . models import *

class NewMovieWatchListForm(forms.ModelForm):
    movie_list_name = forms.CharField(required=True)
    movies = forms.CharField(widget=forms.Textarea(), max_length=4000)
    created_by = forms.CharField(max_length=100)

    class Meta:
        model = MovieWatchList
        fields = ["movie_list_name", "movies", "created_by"]
