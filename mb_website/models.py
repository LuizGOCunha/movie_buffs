from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

