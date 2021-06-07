from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('celeb/', views.celeb, name='celeb'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]