from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/', views.create_profile, name='profile'),

    path('create-trip/', views.create_trip, name='trip'),

    path('find-buddy/', views.find_buddy, name='find_buddy'),

    path(
        'chat/<int:user_id>/',
        views.chat,
        name='chat'
    ),
    path(
    'send-request/<int:user_id>/',
    views.send_request,
    name='send_request'
    ),
    path(   
    'requests/',
    views.requests_page,
    name='requests'
    ),
    path(
    'map/',
    views.map_view,
    name='map'
    ),
    path(
    'expense/',
    views.expense_view,
    name='expense'
    ),

    path(
    'hotels/',
    views.hotels,
    name='hotels'
),

    path(
    'restaurants/',
    views.restaurants,
    name='restaurants'
),
path(
    'restaurants/',
    views.restaurants,
    name='restaurants'
),

path(
    'attractions/',
    views.attractions,
    name='attractions'
),

path(
    'weather/',
    views.weather,
    name='weather'
),

path(
    'transport/',
    views.transport,
    name='transport'
),

path(
    'itinerary/',
    views.itinerary,
    name='itinerary'
),

path(
    'packing/',
    views.packing,
    name='packing'
),

path(
    'ai-trip-planner/',
    views.ai_trip_planner,
    name='ai_trip_planner'
),
path(
    'ai-trip/',
    views.ai_trip_planner,
    name='ai_trip',
),
]