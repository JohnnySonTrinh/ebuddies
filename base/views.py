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


# This function is used to display the login page.
def loginPage(request):
    # This is the page that the user will be redirected to after logging in.
    page = 'login'
    # If the user logged in, they will be redirected to the home page.
    if request.user.is_authenticated:
        return redirect('home')  # Redirects to the home page.

    # If the user is not logged in, the login form will be displayed.
    if request.method == 'POST':
        # The username and password are retrieved from the form.
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # The user is authenticated using the username and password.
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:  # Specify the exception
            messages.error(request, 'Username does not exist')
        # Logged in and redirected to the home page.
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome ' + username)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    # The context dictionary is used to pass data to the template.
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


# This function is used to log out the user.
def logoutUser(request):
    logout(request)  # Logs out the user.
    return redirect('home')  # Redirects to the home page.


# This function is used to display the registration page.
def registerPage(request):
    # If the user is logged in, they will be redirected to the home page.
    form = UserCreationForm()

    # If the user is not logged in, the registration form will be displayed.
    if request.method == 'POST':
        # The form is populated with the data entered by the user.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        # If the form is not valid, an error message is displayed.
        else:
            messages.error(
                request, 'An error has occurred during registration'
            )

    # The context dictionary is used to pass data to the template.
    return render(request, 'base/login_register.html', {'form': form})


# This function is used to display the home page.
def home(request):
    # The search query is retrieved from the URL.
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    # The threads are filtered based on the search query.
    threads = Thread.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    # The first five topics are retrieved from the database.
    topics = Topic.objects.all()[0:5]
    thread_count = threads.count()
    comments = Message.objects.all().filter(
        Q(thread__topic__name__icontains=q)
    )

    # The context dictionary is used to pass data to the template.
    context = {
        'threads': threads,
        'topics': topics,
        'thread_count': thread_count,
        'comments': comments
    }
    return render(request, 'base/home.html', context)


# This function is used to display the thread page.
def thread(request, pk):
    # The thread is retrieved from the database.
    thread = Thread.objects.get(id=pk)
    comments = thread.message_set.all()
    participants = thread.participants.all()

    # User submits a comment, the comment is created and added to the thread.
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            thread=thread,
            body=request.POST.get('body')
        )
        thread.participants.add(request.user)
        messages.success(request, 'Your comment has been posted')
        return redirect('thread', pk=thread.id)

    # The context dictionary is used to pass data to the template.
    context = {
        'thread': thread,
        'comments': comments,
        'participants': participants
    }
    return render(request, 'base/thread.html', context)


# This function is used to display the user profile page.
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    threads = user.thread_set.all()
    comments = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        'user': user,
        'threads': threads,
        'comments': comments,
        'topics': topics
    }
    return render(request, 'base/profile.html', context)


# This function is used to display the create thread page.
@login_required(login_url='login')
def createThread(request):
    form = ThreadForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        thread = Thread.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        messages.success(request, 'Thread has been created')
        return redirect('thread', thread.id)

    context = {'form': form, 'topics': topics}
    return render(request, 'base/thread_form.html', context)


# This function is used to update a thread.
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


# This function is used to delete a thread.
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

    return render(request, 'base/delete.html', {'obj': thread})


# This function is used to delete a comment.
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


# This function is used to update a user.
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


# This function is used to display the topics page.
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})


def activityPage(request):
    comments = Message.objects.all()
    return render(request, 'base/activity.html', {'comments': comments})
