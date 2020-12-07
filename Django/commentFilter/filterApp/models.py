from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import ForeignKey


class User(models.Model) :
    user_email = models.EmailField(unique=True)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)


class Text(models.Model):
    content = models.CharField(max_length=400)

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=User)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'timeline_photo/%Y/%m/%d')
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __Str__(self):
        return "text : " + self.text

    class Meta:
        ordering = ['-created']


# class Comment(models.Model):
#     photo = models.ForeignKey(Photo)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=User)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


