from django.urls import path, include
from candidates.views import show_all_candidate, show_tasks, task_solution

app_name = 'candidate'


urlpatterns = [
    path('', show_all_candidate, name='show_all_candidate'),
    path('candidate-tasks/<int:candidate_id>/', show_tasks, name='show_tasks'),
    path('task-solution/<int:task_id>/', task_solution, name='task_solution'),

]