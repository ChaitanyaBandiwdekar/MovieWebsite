from django.db import models

# Create your models here.
class Movie:
    img: str
    name: str
    release_date = int

    def __init__(self, img, name, release_date) -> None:
        self.img = img
        self.name = name
        self.release_date = release_date