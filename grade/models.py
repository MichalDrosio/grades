from django.db import models

# Create your models here.
from django.urls import reverse

from candidates.models import Candidate
from recruiters.models import Recruiter
from tasks.models import Task


class Grade(models.Model):
    VALUE = [(i, str(i)) for i in range(1, 6)]
    value = models.PositiveIntegerField(choices=VALUE, verbose_name='Ocena', blank=True)
    candidate = models.ForeignKey(Candidate, related_name='student', on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, related_name='judge', on_delete=models.CASCADE, blank=True)
    task = models.ForeignKey(Task, related_name='question', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('recruiters:judge_task_candidate', args=[self.id])