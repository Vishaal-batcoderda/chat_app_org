from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=20, blank=True, null=True)  # Sentiment label
    sentiment_score = models.FloatField(blank=True, null=True)  # Sentiment score

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'
