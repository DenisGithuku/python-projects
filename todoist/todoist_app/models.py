from django.db import models


# Create your models here.
class Task(models.Model):
    id = models.IntegerField(auto_created=True, primary_key = True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    due_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    tasks = models.Manager()
