from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_torrents/', views.all_torrents, name='all_torrents'),
    path('my_torrents/', views.my_torrents, name='my_torrents'),
    path('torrents/<int:torrent_id>/', views.torrent, name='torrent'),
    path('torrents/delete/<int:torrent_id>/', views.torrent_delete, name='torrent_delete'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload, name='upload'),
]