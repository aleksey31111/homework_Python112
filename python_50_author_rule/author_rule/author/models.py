from django.db import models


class Author(models.Model):
    fio = models.CharField(max_length=40, blank=False)
    born_date = models.DateField()
    email = models.EmailField(blank=False)
    name_project = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=30)


class Rule(models.Model):
    name = models.CharField(max_length=30)
    rules = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='rule/images/')


