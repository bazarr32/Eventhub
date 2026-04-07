from django.db import models
from django.db import models
from django.conf import settings
from events.models import Event


User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} -> {self.event}"

# Create your models here.
