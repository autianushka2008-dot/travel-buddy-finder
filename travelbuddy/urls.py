from django.contrib import admin
from django.urls import include, path
from buddy import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/', views.create_profile, name='profile'),
    path('create-trip/', views.create_trip, name='trip'),
    path('find-buddy/', views.find_buddy, name='find_buddy'),



    path('admin/', admin.site.urls),
    path('', include('buddy.urls')),
]
