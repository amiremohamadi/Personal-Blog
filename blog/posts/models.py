from django.db import models

class Post(models.Model):
    tag = models.CharField(max_length=20)
    header = models.CharField(max_length=40)
    content = models.TextField()
    time = models.DateField(auto_now_add=True, auto_now=False) # for adding post (not update)
    
    def __str__(self):
        return self.header