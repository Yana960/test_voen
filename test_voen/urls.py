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
from django.conf import settings
from django.conf.urls.static import static
import velo.views
import object.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', velo.views.showmain, name='showmain'),
    path('articles/', velo.views.articles, name='articles'),
    path('/about', velo.views.about, name='about'),
    path('/objects', object.views.showobject, name='objects'),
    path('/navigator', velo.views.navigator, name='navigator'),
    path('/saved', velo.views.saved, name='saved'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)