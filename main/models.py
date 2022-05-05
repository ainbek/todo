from  django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
class ToMeet(models.Model):
    persone = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)
    date_of_meeting = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
class Goal_for_month(models.Model):
    MONTHS_CHOICES = [
    ('1', 'январь'),
    ('2', 'февраль'),
    ('3', 'март'),
    ('4', 'апрель'),
    ('5', 'май'),
    ('6', 'июнь'),
    ('7', 'июль'),
    ('8', 'август'),
    ('9', 'сентябрь'),
    ('10', 'октябрь'),
    ('11', 'ноябрь'),
    ('12', 'декабрь')
]
    goal = models.CharField(max_length=255)
    month = models.CharField(max_length=2, choices=MONTHS_CHOICES, default='1',   )
    difficulty = models.PositiveSmallIntegerField()
    reason_for_goal = models.TextField()



