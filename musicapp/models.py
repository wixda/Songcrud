from datetime import datetime
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=300, default='Lyrics not available')

    def __str__(self):
        return self.song_id