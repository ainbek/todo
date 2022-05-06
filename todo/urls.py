"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from unicodedata import name
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
#from main.views import delet 
from main.views import * 
from main.views import ToMeet
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home" ),
    path("test/", test, name="test"),
    path("test2/", second),
    #path("test2/", test2, name="test2"),
    path("add-todo/", add_todo, name="add-todo"), 
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),
    path("fav-todo/<id>/", fav_todo,  name="fav-todo"), 
    path("unfav-todo/<id>/", unfav_todo,  name="unfav-todo"),
    path("close-todo/<id>/", close_todo, name="close-todo"),  
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

