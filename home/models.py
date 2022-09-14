from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class URL(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    url_link = models.URLField(max_length=200)
    short_code = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"{self.url_link}"
    
    def get_absolute_url(self):
        return reverse("short_code", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)