from django.shortcuts import render, redirect
from django.contrib import messages
from candidates.models import Candidate
from grade.models import Grade
from recruiters.forms import CreateTaskForm, AddTaskCandidateForm, JudgeTaskForm
from recruiters.models import Recruiter
# Create your views here.



def index(request):
    return render(request, 'base.html')


def show_all_recruiters(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'recruiters/all_recruiters.html', {'recruiters': recruiters})


def detail_recruiter(request, recruiter_id):
    recruiter = Recruiter.objects.get(pk=recruiter_id)
    return render(request, 'recruiters/recruiter.html', {'recruiter': recruiter})


def add_task(request):
    add_task_form = CreateTaskForm(request.POST)
    if request.method == 'POST':
        if add_task_form.is_valid():
            add_task_form.save()

            return redirect('tasks:show_all_task')
    else:
        add_task_form = CreateTaskForm()

    return render(request, 'recruiters/add_task.html', {'add_task_form': add_task_form})


def add_task_to_candidate(request):
    if request.method == 'POST':
        form_grade = AddTaskCandidateForm(request.POST)
        if form_grade.is_valid():
            form_grade.save()
            return redirect('recruiters:add_task_to_candidate')

    else:
        form_grade = AddTaskCandidateForm()
    return render(request, 'recruiters/task_to_candidate.html', {'form_grade': form_grade})


def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'recruiters/candidate_list.html', {'candidates': candidates})


def show_task_candidate(request, candidate_id):
    candidate = Candidate.objects.get(pk=candidate_id)
    garde = Grade.objects.filter(candidate_id=candidate)
    return render(request, 'recruiters/candidate_tasks_list.html', { 'candidate': candidate, 'garde': garde})


def judge_task_candidate(request, grade_id):
    grade = Grade.objects.get(pk=grade_id)

    if request.method == 'POST':
        form_judge = JudgeTaskForm(request.POST, instance=grade)
        if grade.value:
            messages.error(request, 'zadanie bylo juz oceniane')
        else:
            if form_judge.is_valid():
                form_judge.save()
                messages.success(request, 'zadanie oceniane')
                redirect('recruiters:candidate_list')

    else:
        form_judge = JudgeTaskForm()
    return render(request, 'recruiters/judge_tasks.html', {'form_judge': form_judge, 'grade': grade})