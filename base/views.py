from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home page!')

def thread(request):
    return HttpResponse('Thread page!')