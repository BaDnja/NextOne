from django import forms
from .models import Torrent, Genre

class TorrentForm(forms.Form):
    genres = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Genre.objects.all().values_list("pk", "name"))