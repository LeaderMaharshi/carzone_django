from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
       
    search_fields = ('car_title', 'city', 'color', 'year')
    list_display = ('id', 'car_title', 'city', 'color', 'year', 'price', 'is_featured')
    list_display_links = ('car_title', 'city', 'color', 'year' )
    list_editable = ('is_featured',)
    list_filter = ('car_title', 'city', 'color', 'year')
    


admin.site.register(Car, CarAdmin)