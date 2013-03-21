# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'furart/index.html')

def signup(request):
    return render(request, 'furart/signup.html');

