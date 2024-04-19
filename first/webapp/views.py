# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render

# Create your views here.
#from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie


def index(request):
 #   return HttpResponse("<H2>HEY! Welcome... </H2><br><H3> Abhishek </H3>")

    all_movies = Movie.objects.all()
    context = {
        'all_movies': all_movies,
    }
    return render(request, 'webapp/index.html', context)


def detail(request, movie_id):
    #return HttpResponse("<h2>Welcome to ID : " + str(movie_id) + "</h2>")
    m1=get_object_or_404(Movie, pk=movie_id)
    return render(request, 'webapp/error.html', {'m1': m1})


def favourite(request, movie_id):
    m1 = get_object_or_404(Movie, pk=movie_id)
    try:
        selected_songs = m1.songs_set.get(pk=request.POST['songs'])
    except(KeyError, Songs.DoesNotExist):
        return render(request, 'webapp/error.html', {'m1': m1, 'error_message': "Song is not selected"})
    else:
        selected_songs.is_favourite=True
        selected_songs.save()
        return render(request, 'webapp/error.html', {'m1': m1})