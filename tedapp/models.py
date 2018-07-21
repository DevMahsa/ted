

from django.db import models

class Url(models.Model):
    title = models.CharField(max_length=500, null=True)
    event = models.CharField(max_length=500, null=True)
    low = models.CharField(max_length=500 ,null=True)
    medium= models.CharField(max_length=500 ,null=True)
    high = models.CharField(max_length=500, null=True)
    fasub = models.CharField(max_length=500, null=True)
    engsub = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title

class FarsiTed(models.Model):
    link = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.link

class Football(models.Model):
    match = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.match
