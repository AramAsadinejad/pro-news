from django.db import models
from django.contrib.auth.models import User


class news(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='images/')
    reporter=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.title