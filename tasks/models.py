from django.db import models

# Create your models here.
from django.urls import reverse

from candidates.models import Candidate
from recruiters.models import Recruiter


class Task(models.Model):
    title = models.CharField(max_length=20, verbose_name='Tytuł zadania')
    content = models.TextField(verbose_name='Treść')
    answer = models.TextField(blank=True, help_text='Podaj swoją odpowiedź')

    class Meta:
        index_together = (('id',),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('candidate:task_solution', args=[self.id])