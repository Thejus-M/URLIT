from django.db import models
from django.contrib.auth.models import User
import string
import random

class URL(models.Model):

    url_link=models.URLField(max_length=200)
    random_endpoint = random.choice(string.ascii_letters)
    short_code=models.CharField(max_length=50,default=random_endpoint)
    
    class Meta:
        verbose_name = "url"
        verbose_name_plural = "urls"
    def __str__(self):
        return self.url_link



class UserData(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "UserData"
        verbose_name_plural = "UserData Details"
    def __str__(self):
        return self.name
