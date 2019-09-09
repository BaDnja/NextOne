from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_torrents', views.all_torrents, name='all_torrents'),
    path('my_torrents', views.my_torrents, name='my_torrents'),
    path('upload', views.upload, name='upload'),
]