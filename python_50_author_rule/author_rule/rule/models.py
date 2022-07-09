from django.db import models


class Rule(models.Model):
    name = models.CharField(max_length=30)
    rules = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='rule/images/')
