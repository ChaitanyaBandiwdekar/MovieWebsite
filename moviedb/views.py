from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):

    movies = []

    movie1 = Movie('img1.jpeg', 'Black Panther', 2018)
    movie2 = Movie('img2.jpeg', 'After', 2017)
    movie3 = Movie('img3.jpeg', 'Joker', 2019)
    movie4 = Movie('img4.jpeg', 'Spiderman', 2017)
    movie5 = Movie('img5.jpeg', 'Assassin', 2014)
    movie6 = Movie('img6.jpeg', 'Captain America', 2015)

    movies = [movie1, movie2, movie3, movie4, movie5, movie6]

    return render(request, 'cap_homepage.html', {'movies': movies})