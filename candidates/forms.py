from django import forms

from tasks.models import Task


class TaskSolutionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['answer']