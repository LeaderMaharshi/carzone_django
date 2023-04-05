from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    Designation = models.CharField(max_length=250)
    photos = models.ImageField(upload_to='photos/teams')
    facebook_links = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    google_plus = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    