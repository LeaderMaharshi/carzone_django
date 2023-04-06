from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50px; " width="40"/>'.format(object.photos.url))
    
    thumbnail.short_description = 'Photo'
    
    search_fields = ('first_name', 'last_name', 'Designation')
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'Designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name', 'last_name')
    list_filter = ('Designation', )
# Register your models here.
admin.site.register(Team, TeamAdmin)
