from djongo import models

# Create your models here.
class (models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
