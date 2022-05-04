from cgitb import text
from  django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    persone = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)
    date_of_meeting = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

