from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):

    Genre_Choice = (
            ('Pop', 'Pop'),
            ('Rock', 'Rock'),
            ('Blues', 'Blues'),
            ('Vocal', 'Vocal'),
            ('Gospel', 'Gospel'),
            ('Jazz', 'Jazz'),
            ('Country', 'Country'),
            ('Classical music', 'Classical music'),
            ('Musical', 'Musical'),
            ('Pop', 'Pop'),
            ('Hip Hop', 'Hip Hop'),
            ('Chanson', 'Chanson')
          )


    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=Genre_Choice, default='Pop')
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    released_year = models.IntegerField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_title + '-' + self.artist
