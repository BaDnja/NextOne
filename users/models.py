from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.name