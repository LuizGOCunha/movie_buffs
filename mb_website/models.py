from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=500)
    overview = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()

