from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from buddy.forms import RegisterForm
def home(request):

    return render(
        request,
        'home.html'
    )