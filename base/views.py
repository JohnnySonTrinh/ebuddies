from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Thread, Topic
from .forms import ThreadForm

# Create your views here.

#threads = [
#    {'id': 1, 'name': 'League of Legends'},
#    {'id': 2, 'name': 'Valorant'},
#    {'id': 3, 'name': 'Teamfight Tactics'},
#]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all()
    thread_count = threads.count()

    context = {'threads': threads, 'topics': topics, 'thread_count': thread_count}
    return render(request, 'base/home.html', context)

def thread(request, pk):
    thread = Thread.objects.get(id=pk)
    context = {'thread': thread}
    return render(request, 'base/thread.html', context)

def createThread(request):
    form = ThreadForm()

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/thread_form.html', context)

def updateThread(request, pk):
    thread = Thread.objects.get(id=pk)
    form = ThreadForm(instance=thread)

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/thread_form.html', context)


def deleteThread(request, pk):
    thread = Thread.objects.get(id=pk)

    if request.method == 'POST':
        thread.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':thread})