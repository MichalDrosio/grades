from django.shortcuts import render

# Create your views here.
from tasks.models import Task


def show_all_task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/all_tasks.html', {'tasks': tasks})

