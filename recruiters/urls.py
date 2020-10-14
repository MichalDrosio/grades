from django.urls import path
from recruiters.views import show_all_recruiters, index, detail_recruiter, add_task, add_task_to_candidate, \
    candidate_list, show_task_candidate, judge_task_candidate

app_name = 'recruiters'


urlpatterns = [
    path('', index, name='index'),
    path('recruiters/', show_all_recruiters, name='show_all_recruiters'),
    path('recruiter/<int:recruiter_id>/', detail_recruiter, name='detail_recruiter'),
    path('taskcandidate/', add_task_to_candidate, name='add_task_to_candidate'),
    path('add-task/', add_task, name='add_task'),
    path('candidates/', candidate_list, name='candidate_list'),
    path('tasks-candidate/<candidate_id>/', show_task_candidate, name='show_task_candidate'),
    path('judge-task/<int:grade_id>/', judge_task_candidate, name='judge_task_candidate'),

]