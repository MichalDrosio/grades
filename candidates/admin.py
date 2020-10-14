from django.contrib import admin

# Register your models here.
from candidates.models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']