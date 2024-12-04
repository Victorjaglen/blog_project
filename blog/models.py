from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now=True)
    banner = models.ImageField(default='fallback.jpg', blank=True)

    def __str__(self):
        return self.title
