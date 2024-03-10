from django.shortcuts import render
from .models import Thread

# Create your views here.

#threads = [
#    {'id': 1, 'name': 'League of Legends'},
#    {'id': 2, 'name': 'Valorant'},
#    {'id': 3, 'name': 'Teamfight Tactics'},
#]

def home(request):
    threads = Thread.objects.all()
    context = {'threads': threads}
    return render(request, 'base/home.html', context)

def thread(request, pk):
    thread = Thread.objects.get(id=pk)
    context = {'thread': thread}
    return render(request, 'base/thread.html', context)