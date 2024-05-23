"""imports"""
from datetime import date

from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
# BUG: could be changed to namedtupel here, because it only stores data
# BUG: If there is the option to add people to a chat, namedtupel isnt an option anymore
class Chat(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    text = models.CharField(max_length=500) 
    created_at = models.DateTimeField(default=timezone.now)
    chat = models.ForeignKey(Chat,
                             on_delete=models.CASCADE,
                             related_name='chat_message_set',
                             default=None,
                             blank=True,
                             null=True
                             )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='author_message_set'
                               )
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='receiver_message_set'
                                 )
    def __str__(self):
        return f"{self.text} by {self.author} at {self.created_at}"
