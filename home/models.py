from django.db import models
from django.contrib.auth.models import User
import string
import random


class URL(models.Model):

    url_link = models.URLField(max_length=200)

    def random_endpoint():
        random_string = ''
        for _ in range(10):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))
        return random_string

    short_code = models.CharField(max_length=50, default=random_endpoint())

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
        return self.name.username
