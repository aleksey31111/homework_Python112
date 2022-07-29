from django.db import models


class Secondpage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name='Контент')
    date = models.DateField(verbose_name='День создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Framework статья"
        verbose_name_plural = "Framework статьи"
