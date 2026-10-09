from django.contrib import admin
from .models import Profile, Trip
from .models import Message

admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Trip)
