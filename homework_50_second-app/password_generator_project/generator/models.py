from django.db import models

class Generator(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='sklls/images/')
    url = models.URLField(blank=True)
