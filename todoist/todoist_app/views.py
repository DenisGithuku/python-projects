from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home_view(request):
    tasks = Task.tasks.all().values()
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context = context)


def edit_view(request, id):
    task = Task.tasks.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'edit.html', context)


def add_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add.html', {'form': form})

def delete_view(request, id):
    task = Task.tasks.get(id = id)
    task.delete()
    return redirect('home')

def sort_view(request, sort_type):
    tasks = Task.tasks.all()
    if sort_type == 1:
        tasks = tasks.order_by('-id')
    if sort_type == 0:
        tasks = tasks.order_by('id')
    return render(request, 'home.html', {'tasks': tasks})