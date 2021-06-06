from django.db import models

# Create your models here.
class Movie(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    release_date = models.IntegerField()

    # def __init__(self, img, name, release_date) -> None:
    #     self.img = img
    #     self.name = name
    #     self.release_date = release_date