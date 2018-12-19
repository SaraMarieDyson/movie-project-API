"""Moviewatchlist URL Configuration.

Lists URL routes.
"""
from django.conf.urls import url
from django.contrib import admin

from movies import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^movies/$', views.movie_list, name="movie_list"),
    url(r'^movies/(?P<pk>\d+)/$', views.movies_detail, name="movies_detail"),
    url(r'^movie_watch_list/$', views.create_movie_watch_list,
        name="create_movie_watch_list"),
    url(r'^movie_watch_list/(?P<pk>\d+)/$', views.movie_watch_list,
        name="movie_watch_list"),
    url(r'^admin/', admin.site.urls),
]
