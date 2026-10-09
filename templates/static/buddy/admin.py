from django.contrib import admin

from .models import *

admin.site.register(Profile)
admin.site.register(Trip)
admin.site.register(MatchRequest)
admin.site.register(Review)