from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    age = models.IntegerField()

    city = models.CharField(
        max_length=100
    )

    bio = models.TextField()

    budget = models.IntegerField()

    interests = models.TextField()

    travel_style = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.user.username


class Trip(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    destination = models.CharField(
        max_length=200
    )

    start_date = models.DateField()

    end_date = models.DateField()

    budget = models.IntegerField()

    trip_type = models.CharField(
        max_length=100
    )

    interests = models.TextField()

    def __str__(self):
        return self.destination