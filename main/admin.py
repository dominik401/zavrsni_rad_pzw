from django.contrib import admin
from .models import *

model_list = [Reminder, Project, Category, Task, TimeLog]
admin.site.register(model_list)