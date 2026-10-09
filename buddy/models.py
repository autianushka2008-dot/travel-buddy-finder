from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField()
    city = models.CharField(max_length=100)
    bio = models.TextField()
    budget = models.IntegerField()
    interests = models.TextField()
    travel_style = models.CharField(max_length=100)
    profile_image = models.ImageField(
        upload_to='profiles/',
        default='default.jpg'
    )
    latitude = models.FloatField(
        null=True,
        blank=True
    )
    longitude = models.FloatField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username


class Trip(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    destination = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField()

    budget = models.IntegerField()

    trip_type = models.CharField(max_length=100)

    interests = models.TextField()

    def __str__(self):
        return self.destination


class FriendRequest(models.Model):

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_requests'
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_requests'
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )


class Message(models.Model):

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )

    message = models.TextField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )
class Review(models.Model):

    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_given'
    )

    reviewed_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_received'
    )

    rating = models.IntegerField()

    comment = models.TextField()
class GroupTrip(models.Model):

    trip_name = models.CharField(
        max_length=100
    )

    destination = models.CharField(
        max_length=100
    )

    members = models.ManyToManyField(
        User
    )    