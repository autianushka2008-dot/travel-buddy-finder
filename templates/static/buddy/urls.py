from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'create-trip/',
        views.create_trip,
        name='create_trip'
    ),

    path(
        'matches/',
        views.matches,
        name='matches'
    ),
]