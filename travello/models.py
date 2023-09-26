from django.db import models

# Create your models here.
class Destination(models.Model):
    # id = models.UUIDField()
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media')
    desc = models.TextField()
    price = models.IntegerField()
    offer  = models.BooleanField(default=False)