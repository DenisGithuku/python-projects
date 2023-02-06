from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    field_list = ('title', 'description', 'due_time')

admin.site.register(Task, TaskAdmin)