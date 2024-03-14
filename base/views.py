from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Thread, Topic, Message
from .forms import ThreadForm, UserForm

# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome ' + username)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')
        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred during registration')
        
    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all()
    thread_count = threads.count()
    comments = Message.objects.all().filter(Q(thread__topic__name__icontains=q))

    context = {'threads': threads, 'topics': topics, 'thread_count': thread_count, 'comments': comments}
    return render(request, 'base/home.html', context)

def thread(request, pk):
    thread = Thread.objects.get(id=pk)
    comments = thread.message_set.all()
    participants = thread.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            thread=thread,
            body=request.POST.get('body')
        )
        thread.participants.add(request.user)
        messages.success(request, 'Your comment has been posted')
        return redirect('thread', pk=thread.id)

    context = {'thread': thread, 'comments': comments, 'participants': participants}
    return render(request, 'base/thread.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    threads = user.thread_set.all()
    comments = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'threads': threads, 'comments': comments, 'topics': topics}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createThread(request):
    form = ThreadForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name) 
        
        Thread.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Thread has been created')
        return redirect('thread', pk=Thread.objects.last().id)
        
    context = {'form': form, 'topics': topics}
    return render(request, 'base/thread_form.html', context)

@login_required(login_url='login')
def updateThread(request, pk):
    thread = Thread.objects.get(id=pk)
    form = ThreadForm(instance=thread)
    thread_topic = thread.topic.name
    topics = Topic.objects.all()
    if request.user != thread.host:
        # change this to a return
        messages.error(request, 'You are not allowed here!')
        return redirect('home')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name) 
        thread.name = request.POST.get('name')
        thread.description = request.POST.get('description')
        thread.topic = topic
        thread.save()
        messages.success(request, 'Thread has been updated')
        return redirect('home')

    context = {'form': form, 'topics': topics, 'thread_topic': thread_topic}
    return render(request, 'base/thread_form.html', context)

@login_required(login_url='login')
def deleteThread(request, pk):
    thread = Thread.objects.get(id=pk)

    if request.user != thread.host:
        messages.error(request, 'You are not allowed here!')
        return redirect('home')

    if request.method == 'POST':
        thread.delete()
        messages.success(request, 'Thread has been deleted')
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':thread})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        messages.error(request, 'You are not allowed here!')
        return redirect('home')
    
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message has been deleted')
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been updated')
            return redirect('user-profile', pk=user.id)
        
    return render(request, 'base/update_user.html', {'form': form})
