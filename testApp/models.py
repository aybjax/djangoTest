from django.db import models


# Create your models here.
from django.urls import reverse


class TestModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    nbr = models.FloatField()

    def __str__(self):
        return f'{self.name}:    {self.email}'

    # def get_absolute_url(self):
    #     return '/'
