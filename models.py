from django.db import models


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20, blank=True)
    description = models.CharField(blank=True, max_length=35)
    image = models.ImageField

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    cover = models.URLField(blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=20)
    cover = models.URLField(blank=True)
    lyrics = models.TextField(blank=True)
    duration = models.DurationField()
    source = models.URLField(blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_songs')
    listened = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
