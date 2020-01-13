from django.db import models

# Create your models here.

class Posteos(models.Model):
    """docstring for Posteos."""
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='blog',null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
