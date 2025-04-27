from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    likes = models.PositiveBigIntegerField(default=0)


class User(models.Model):
    pass