
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', default='/media/images/teste.jpeg')
    
    def to_json_dict(self):
        return {
            'image': self.image.url
        }

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class image(models.Model):
    image = models.ImageField(
        upload_to='images/', default='/media/images/teste.jpeg')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.image

class Setor(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/setor/', default='/media/images/teste.jpeg'
    )
    slug = models.SlugField(max_length=200, unique=True, default=None, blank=True, null=True)
    def to_dict_json(self):
        return {
            'title': self.title,
            'image': self.image.url,
            'slug' : self.slug
        }
    def __str__ (self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/setor/', default='/media/images/teste.jpeg')
    setor = models.ForeignKey(
        Setor, on_delete = models.CASCADE, related_name="setores", default=None, blank=True, null=True
    )
    def to_dict_json(self):
        return {
            'title': self.title,
            'image': self.image.url
        }
    def __str__ (self):
        return self.title

