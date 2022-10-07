"""Account View"""
from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    """ Index page """
    #return HttpResponse("Hello, world. You're at the ACCOUNT index.")
    return render(request, 'account/index.html')
