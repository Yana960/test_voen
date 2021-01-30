from django.urls import path
from . import views
from object import views
from registration import views
from articles import views
urlpatterns = [
	path('', views.showmain, name='showmain'),
	path('/articles', articles.views.showarticles, name='articles'),
	path('/articles/<int:article_id>/', articles.views.specific_article, name='specific_article'),
	path('/about', views.about, name='about'),
	path('/objects', object.views.showobject, name='objects'),
	path('/registration', registration.views.signup, name='signup'),
	path('/navigator', views.navigator, name='navigator'),
	path('/saved', views.saved, name='saved'),
]
