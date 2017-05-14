from django.db import models

class Pools(models.Model):
    name = models.ForeignKey('auth.User')
    poll = models.BooleanField(default=False)

    def __str__(self):
        return self.name.username

class poll(models.Model):
    name = models.ForeignKey('member')
    poll = models.BooleanField(default=False)

    def __str__(self):
        return self.name.name

class member(models.Model):
    name = models.CharField(max_length=200)
    alamat_palsu = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
