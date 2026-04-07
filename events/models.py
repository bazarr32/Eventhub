from django.db import models
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=150)
    capacity = models.PositiveIntegerField()

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    categories = models.ManyToManyField(Category, related_name='events')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user} joined {self.event}"
# Create your models here.
