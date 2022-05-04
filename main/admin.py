from django.contrib import admin
from .models import ToDo
from .models import ToMeet, Goal_for_month

admin.site.register(ToDo)

admin.site.register(ToMeet)
admin.site.register(Goal_for_month) 

