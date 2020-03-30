from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Message(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_by = models.CharField(max_length=200, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + "..."
    
    def get_absolute_url(self):
        return f"send_message/{owner.username}"