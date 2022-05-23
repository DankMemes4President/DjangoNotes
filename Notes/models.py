from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()


class Tag(models.Model):
    title = models.CharField(max_length=100)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
