from django.db import models
from os import path

class Post(models.Model):
    head_image = models.FileField(blank=True)
    tag = models.CharField(max_length=20)
    header = models.CharField(max_length=40)
    content = models.TextField()
    time = models.DateField(auto_now_add=True, auto_now=False) # for adding post (not update)

    def __str__(self):
        return self.header

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField()

    def __str__(self):
        return self.post.header