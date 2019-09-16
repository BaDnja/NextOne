from django.contrib import admin
from .models import Torrent

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_added', 'is_downloaded')
    list_display_links = ('id', 'title')
    list_filter = ('is_downloaded', 'date_added')
    list_editable = ('is_downloaded',)
    search_fields = ('title', 'date_added')
    list_per_page = 25

admin.site.register(Torrent, ListingAdmin)