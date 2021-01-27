from django.urls import path
from . import views
from object import views
urlpatterns = [
	path('', views.showmain, name='showmain'),
	path('/articles', views.articles, name='articles'),
	path('/about', views.about, name='about'),
	path('/objects', object.views.showobject, name='objects'),
	path('/navigator', views.navigator, name='navigator'),
	path('/saved', views.saved, name='saved'),
]
