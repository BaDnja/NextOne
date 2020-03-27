from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Torrent(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    date_added = models.DateField(default=datetime.now, blank=True)
    is_downloaded = models.BooleanField(default=False)
    primary_subtitle = models.CharField(max_length=200, blank=True)
    secondary_subtitle = models.CharField(max_length=200, blank=True)
    for_parents = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    genres = models.ManyToManyField("torrents.Genre")

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name