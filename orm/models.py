from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='aaa.png', blank=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, default=None)


    def __str__(self):
        return self.author.username if self.author else "No Author"

