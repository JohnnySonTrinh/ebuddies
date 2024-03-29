from django.urls import path
from . import views

# The urlpatterns list is used to define the URL patterns for the app.
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('thread/<str:pk>/', views.thread, name='thread'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('create-thread/', views.createThread, name='create-thread'),
    path('update-thread/<str:pk>/', views.updateThread, name='update-thread'),
    path('delete-thread/<str:pk>/', views.deleteThread, name='delete-thread'),
    path(
        'delete-message/<str:pk>/',
        views.deleteMessage,
        name='delete-message'
    ),
    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
]
