# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Movie, Songs
admin.site.register(Movie)

admin.site.register(Songs)
