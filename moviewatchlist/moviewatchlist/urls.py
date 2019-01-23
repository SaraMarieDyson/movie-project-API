"""Moviewatchlist URL Configuration.

Lists URL routes.
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from movies import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # url(r'^$', views.home, name='home'),
    url(r'^movies/$', views.movie_list, name="movie_list"),
    url(r'^movies/(?P<pk>\d+)/$', views.movies_detail, name="movies_detail"),
    url(r'^movie_watch_list/$', views.create_movie_watch_list,
        name="create_movie_watch_list"),
    url(r'^movie_watch_list/(?P<pk>\d+)/$', views.movie_watch_list,
        name="movie_watch_list"),
    url(r'^admin/', admin.site.urls),
]
