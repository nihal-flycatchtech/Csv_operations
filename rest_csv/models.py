from django.db import models


class File(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
