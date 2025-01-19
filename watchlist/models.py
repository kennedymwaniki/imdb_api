from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

# this is a movie db model

# watchlist/Movie is a table that has a foreign key to the StreamPlatform table


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


class Review(models.Model):
    # user who created the review
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # a review can only be on one movie, while a movie can have many reviews
    watchlist = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return str(self.rating) + "-" + self.watchlist.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
