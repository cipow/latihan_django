from django.db import models

class ContactMe(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    no_hp=models.CharField(max_length=15)
    message=models.TextField()
