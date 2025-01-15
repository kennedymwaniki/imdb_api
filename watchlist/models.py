from django.db import models

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

# this is a movie db model


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    # a movie can only be on one platform, while a platform can have many movies
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
