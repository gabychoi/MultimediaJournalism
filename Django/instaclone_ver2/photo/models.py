from time import timezone

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')	# User에 종속.
    photo   = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')	# Image/Media
    text    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering    = ['-updated']

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")



