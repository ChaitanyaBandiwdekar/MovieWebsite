from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Chaitanya'})

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])

    ans = a+b

    return render(request, 'result.html', {'ans':ans})