from django.urls import path, re_path
from .views import *


urlpatterns = [
	path('', index),
	path('index', index),
	path('create', create),
	re_path(r'^details/(?P<fid>[0-9]+)$', details),
	re_path(r'^edit/(?P<fid>[0-9]+)$', edit),
	re_path(r'^delete/(?P<fid>[0-9]+)$', delete),
]