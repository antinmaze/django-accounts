"""Account View"""
import json
from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    """ Index page """
    #return HttpResponse("Hello, world. You're at the ACCOUNT index.")
    return render(request, 'account/index.html')


def loadcountries(json_file):
    """ Load Countries """
    json_data = loadjson(json_file)


def loadjson(json_file):
    """ Load Json """
    # Python program to read json file
    # Opening JSON file
    file = open(json_file,"r", encoding='UTF-8')
    # returns JSON object as a dictionary
    json_data = json.load(file)
    # Iterating through the json list
    #for i in data['emp_details']:
    #    print(i)
    # Closing file
    file.close()
    return json_data

