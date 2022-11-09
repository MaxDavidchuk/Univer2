from django.urls import path
from .views import *


urlpatterns = [
	path('reg', reg),
    path('confirm', confirm),
    path('entry', entry),
    path('exit', exit),
    path('profile', profile),
    path('reset', reset),
]