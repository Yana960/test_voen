"""test_voen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import velo.views
import about.views
import navigator.views
import object.views
import registration.views
import articles.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', velo.views.showmain, name='showmain'),
    path('route/', velo.views.showohistorymarsh, name='showohistorymarsh'),
    path('<int:marsh_id>/', velo.views.showohistorymarsh, name='showhistorymarsh'),
    path('/articles', articles.views.showarticles, name='articles'),
    path('/articles/<int:article_id>/', articles.views.specific_article, name='specific_article'),
    path('/about', about.views.about, name='about'),
    path('/objects', object.views.showobject, name='objects'),
    path('/objects/<int:object_id>/', object.views.specific_object, name='specific_object'),
    path('/registration', registration.views.signup, name='registration'),
    path('/navigator', navigator.views.navigator, name='navigator'),
    path('/saved', velo.views.saved, name='saved'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
