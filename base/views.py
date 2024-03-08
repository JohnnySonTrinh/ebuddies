from django.shortcuts import render

# Create your views here.

threads = [
    {'id': 1, 'name': 'League of Legends'},
    {'id': 2, 'name': 'Valorant'},
    {'id': 3, 'name': 'Teamfight Tactics'},
]

def home(request):
    context = {'threads': threads}
    return render(request, 'base/home.html', context)

def thread(request, pk):
    thread = None
    for i in threads:
        if i['id'] == pk:
            thread = i
    context = {'thread': thread}
    return render(request, 'base/thread.html', context)