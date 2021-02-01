from django.urls import path

import about
import articles
import navigator
import registration
from . import views
from about import views
from navigator import views
from object import views
from registration import views
from articles import views

urlpatterns = [
	path('', views.showmain, name='showmain'),
	path('/articles', articles.views.showarticles, name='articles'),
	path('/objects', object.views.showobject, name='objects'),
	path('/registration', registration.views.signup, name='signup'),
	path('/about', about.views.about, name='about'),
	path('/navigator', navigator.views.navigator, name='navigator'),
	path('/saved', views.saved, name='saved'),
]