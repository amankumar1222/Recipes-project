from django.db import models

# Create your models here.
class Rescipe(models.Model):
    title = models.CharField(max_length=700)
    desc = models.TextField()
    url = models.URLField()

