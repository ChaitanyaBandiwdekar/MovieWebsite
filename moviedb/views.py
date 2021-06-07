from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, 'cap_homepage.html', {'movies': movies})

def celeb(request):
    return render(request, 'cap_celebrity.html')

def login(request):
    return render(request, 'cap_login.html')

def signup(request):
    return render(request, 'cap_signup_form.html')