from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from instaclone import settings


class Photo(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "text : "+self.text

    class Meta :
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.id])

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='post')

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'


class Comment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'
