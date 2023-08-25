from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def logout_user(request):
    pass

# Create your views here.
def home(request):
    
    return render(request, 'home.html', {})



