from django.db import models


class PagePp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField
