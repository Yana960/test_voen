from django.urls import path

import about
import navigator
from . import views
from about import views
from navigator import views

urlpatterns = [
	path('', views.showmain, name='showmain'),
	path('/articles', views.articles, name='articles'),
	path('/about', about.views.about, name='about'),
	path('/objects', views.objects, name='objects'),
	path('/navigator', navigator.views.navigator, name='navigator'),
	path('/saved', views.saved, name='saved'),
]