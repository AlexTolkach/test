import datetime

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150, null=False)
    author = models.CharField(max_length=100, null=False)
    year_of_publishing = models.IntegerField(null=False)
    isbn = models.CharField(max_length=17, unique=True, null=False)

    def __str__(self):
        return self.name


class UserLibrary(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=254, null=False)
    date_registered = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

