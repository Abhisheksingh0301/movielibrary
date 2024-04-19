from django.conf.urls import url

from . import views
app_name = 'webapp'
urlpatterns = [
 url(r'^$', views.index, name='index'),

# url(r'^(?<movie_id>[0-9]+)/$', views.detail),


 url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
 url(r'^(?P<movie_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]
