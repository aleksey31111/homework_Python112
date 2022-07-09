from django.db import models


class Author(models.Model):
    fio = models.CharField(max_length=50)
    name_project = models.CharField(max_length=50)
    born_date = models.DateField()
    country = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.title


