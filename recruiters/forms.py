from candidates.models import Candidate
from grade.models import Grade
from tasks.models import Task
from django import forms


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['answer']


class AddTaskForm(forms.Select):
    class Meta:
        model = Task
        fields = ('title',)


class AddCandidateForm(forms.Select):
    class Meta:
        model = Candidate
        fields = ('first_name',)


class AddTaskCandidateForm(forms.ModelForm):
    class Meta:
        model = Grade
        exclude = ('value',)
        widgets = {'task': AddTaskForm, 'candidate': AddCandidateForm}


class JudgeTaskForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['value']
