from django.db import models


class Receita(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    preparo = models.TextField()

    def __str__(self):
        return str(self.title)