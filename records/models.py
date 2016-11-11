from django.db import models
from django.utils import timezone


class HashTag(models.Model):
    name = models.CharField(max_length=10)


class Album(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField(HashTag, blank=True)


class Track(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    tags = models.ManyToManyField(HashTag, blank=True)
