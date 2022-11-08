from django.urls import path
from .views import *


urlpatterns = [
	path('', index),
	path('index', index),
	path('about', about),
	path('contact', contact),
]