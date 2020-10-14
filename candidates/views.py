from django.shortcuts import render, redirect

from candidates.forms import TaskSolutionForm
from candidates.models import Candidate

# Create your views here.
from tasks.models import Task


def show_all_candidate(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/list_candidate.html', {'candidates': candidates})


def show_tasks(request, candidate_id):
    candidate = Candidate.objects.get(pk=candidate_id)
    tasks = Task.objects.filter(question__candidate=candidate)
    return render(request, 'candidates/list_tasks.html', {'candidate': candidate, 'tasks': tasks})


def task_solution(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        solution_form = TaskSolutionForm(request.POST, instance=task)
        if solution_form.is_valid():
            solution_form.save()
            return redirect('candidate:show_all_candidate')
    else:
        solution_form = TaskSolutionForm()
    return render(request, 'candidates/task_solution.html', {'task': task, 'solution_form': solution_form})