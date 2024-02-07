from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images', height_field=None, width_field=None, max_length=None)
    url= models.URLField(blank=True)