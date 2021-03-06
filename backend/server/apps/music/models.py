from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# from django.template.defaultfilters import slugify
# import math
# from time import strftime, gmtime


class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Сценическое имя")
    slug = models.SlugField(verbose_name="Идентификатор")
    artist_pic = models.ImageField(upload_to="pictures/artists", blank=True, default="pictures/artists/default.jpg",
                                   verbose_name="Фото")


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name="Жанр")
    slug = models.SlugField(verbose_name="Идентификатор")
    genre_pic = models.ImageField(upload_to="pictures/genres", blank=True, default="pictures/genres/default.jpg",
                                  verbose_name="Картинка")


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(verbose_name="Идентификатор")
    album_pic = models.ImageField(upload_to="pictures/albums", blank=True, default="pictures/albums/default.jpg",
                                  verbose_name="Картинка")
    artists = models.ManyToManyField(Artist, verbose_name="Исполнители")
    release_date = models.DateField(verbose_name="Дата выхода")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(verbose_name="Идентификатор")
    song_pic = models.ImageField(upload_to="pictures/songs", blank=True, default="pictures/songs/default.jpg",
                                 verbose_name="Картинка")
    song = models.FileField(upload_to="tracks", verbose_name="Трек")
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, verbose_name="Жанр")
    artists = models.ManyToManyField(Artist, verbose_name="Исполнители")
    release_date = models.DateField(verbose_name="Дата выхода")
    size = models.IntegerField(default=0, verbose_name="Размер")
    playtime = models.CharField(max_length=10, default="0.00", verbose_name="Продолжительность")
    text = models.TextField(blank=True, null=True, verbose_name="Текст песни")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Song, self).save(*args, **kwargs)
    #
    # @property
    # def duration(self):
    #     return str(strftime('%H:%M:%S', gmtime(float(self.playtime))))
    #
    # @property
    # def file_size(self):
    #     if self.size == 0:
    #         return "0B"
    #     size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    #     i = int(math.floor(math.log(self.size, 1024)))
    #     p = math.pow(1024, i)
    #     s = round(self.size / p, 2)
    #     return "%s %s" % (s, size_name[i])
