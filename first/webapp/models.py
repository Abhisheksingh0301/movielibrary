# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movie(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    movie_logo = models.CharField(max_length=100)

    def __str__(self):
        return self.actor + '---' + self.actor_movie + '---' + self.genre


class Songs(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_name = models.CharField(max_length=100)
    is_favourite=models.BooleanField(default=False)

    def __str__(self):
        return self.file_type + "---" + self.song_name
