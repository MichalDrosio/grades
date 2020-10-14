from tasks.models import Task
from django import forms


class SolutionTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['answer']