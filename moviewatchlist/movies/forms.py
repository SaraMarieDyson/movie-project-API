from django import forms
from . models import *


class NewMovieWatchListForm(forms.ModelForm):
    movie_list_name = forms.CharField(required=True)
    created_by = forms.CharField(max_length=100)


    class Meta:
        model = MovieWatchList
        fields = [
            "movie_list_name",
            "created_by",
        ]


# NOTE: Want to implement Formset for movies:
# https://docs.djangoproject.com/en/2.1/topics/forms/formsets/
    # 
    # movie_title = forms.CharField(required=True)
    # description = forms.CharField(
    #     required=True,
    #     max_length=4000,
    #     help_text="The max length is 4000"
    # )
    #
    # class Meta:
    #     model = Movie
    #     fields = [
    #         "movie_title",
    #         "description",
    #     ]
