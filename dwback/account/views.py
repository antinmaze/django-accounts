"""Account View"""
from django.shortcuts import render
#from django.http import HttpResponse


def login(request):
    """ Login page """
    return render(request, 'account/login.html')

def register(request):
    """ register page """
    return render(request, 'account/register.html')

def password(request):
    """ Password page """
    return render(request, 'account/password.html')

def account(request):
    """ Account home page """
    return render(request, 'account/index.html')
