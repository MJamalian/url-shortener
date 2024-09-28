from django.db import models

# Create your models here.

class Url(models.Model):
    short_link = models.CharField(max_length=255, unique=True)
    long_link = models.CharField(max_length=255)