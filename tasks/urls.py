from django.urls import path
from tasks.views import show_all_task
app_name = 'tasks'

urlpatterns = [
    path('all-tasks/', show_all_task, name='show_all_task')
]


