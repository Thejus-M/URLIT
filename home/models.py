from django.db import models
from django.contrib.auth.models import User


class URL(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    url_link = models.URLField(max_length=200)
    short_code = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.url_link}"
