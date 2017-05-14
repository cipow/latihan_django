from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='blog/picture',default='blog/picture/no-image.jpg')
    dokumen = models.FileField(upload_to='blog/dokumen')

    def __str__(self):
        return self.name
