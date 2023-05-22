from django.db import models

# Create your models here.

class New(models.Model):
    name = models.CharField( max_length=50)
    content = models.TextField(max_length=400)
    image = models.URLField( max_length=400)
    tittle = models.CharField(max_length=200)