from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def cse(request):
    return HttpResponse("Welcome to CSE page")
def etc(request):
    return HttpResponse("Welcome to ETC page")
def mech(request):
    return HttpResponse("Welcome to MECH page")
def civil(request):
    return HttpResponse("Welcome to CIVIL page")