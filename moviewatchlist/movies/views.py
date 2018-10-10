from django.shortcuts import render
from django.http import HttpResponse

def home_test(request):
    return HttpResponse("Tesing movies!")

# Create your views here.
